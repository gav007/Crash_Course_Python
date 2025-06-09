import subprocess
from youtube_transcript_api import YouTubeTranscriptApi
import textwrap
import os

CHUNK_SIZE = 30000  # Characters per processing chunk
MAX_RETRIES = 3     # Max retries for transcript fetching
MAX_CHUNK_LENGTH = 10000  # Max characters per chunk for summarization

def get_transcript(video_id):
    """Fetch transcript for the given video ID."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        print(f"Transcript fetched ({len(transcript)} entries)")
        return "\n".join(entry['text'] for entry in transcript)
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def chunk_text(text, chunk_size):
    """Split text into chunks respecting natural boundaries."""
    chunks = []
    wrapper = textwrap.TextWrapper(
        width=chunk_size,
        break_long_words=True,
        replace_whitespace=False
    )
    
    # Process paragraphs separately to preserve structure
    for paragraph in text.split('\n\n'):
        while paragraph:
            chunk = wrapper.wrap(paragraph)
            if chunk:
                chunks.append(chunk[0])
                paragraph = paragraph[len(chunk[0]):].lstrip()
            else:
                break
    return chunks

def summarize_with_ollama(text, model="llama3"):
    """Summarize text using Ollama with chunking."""
    if len(text) > MAX_CHUNK_LENGTH:
        chunks = chunk_text(text, MAX_CHUNK_LENGTH)
        summaries = []
        for i, chunk in enumerate(chunks):
            print(f"Summarizing chunk {i+1}/{len(chunks)}")
            summaries.append(summarize_chunk(chunk, model))
        combined = "\n\n".join(summaries)
        return summarize_chunk(combined, model)
    return summarize_chunk(text, model)

def summarize_chunk(text, model):
    """Summarize a single text chunk."""
    prompt = (
        "Create a comprehensive bullet-point summary of this YouTube transcript excerpt:\n\n"
        f"{text}\n\n"
        "Focus on key points, actions, and conclusions. Use plain English and avoid markdown."
    )
    
    try:
        result = subprocess.run(
            [r"C:\Users\gavsm\AppData\Local\Programs\Ollama\ollama.exe", "run", model],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=120  # 2-minute timeout
        )
        if result.returncode != 0:
            print(f"Ollama error: {result.stderr.strip()}")
            return "Summary generation failed"
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Summary timed out"
    except Exception as e:
        print(f"Processing error: {str(e)}")
        return "Summary generation failed"

def main():
    video_id = input("Enter YouTube video ID: ").strip()
    transcript = get_transcript(video_id)
    
    if not transcript:
        print("Transcript not available or video ID invalid.")
        return

    # Save raw transcript
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)
    print("Transcript saved as transcript.txt")

    # Generate summary
    print("Generating summary...")
    summary = summarize_with_ollama(transcript, model="llama3")
    
    # Save summary
    os.makedirs("summaries", exist_ok=True)
    summary_file = f"summaries/{video_id}_summary.txt"
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"Summary saved to {summary_file}")

if __name__ == "__main__":
    main()