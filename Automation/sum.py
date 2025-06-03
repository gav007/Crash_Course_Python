import subprocess
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        print("Transcript entries fetched:", len(transcript))
        # Build a list of lines using a simple for-loop
        lines = []
        for entry in transcript:
            lines.append(entry['text'])  # Add just the text part to the list
        text = "\n".join(lines)  # Join all lines with a newline character
        return text
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None


def summarize_with_ollama(text):
    prompt = f"Summarize the following YouTube transcript in clear bullet points and plain English:\n\n{text}"
    result = subprocess.run(
    [r"C:\Users\gavsm\AppData\Local\Programs\Ollama\ollama.exe", "run", "llama3"],
    input=prompt,
    capture_output=True,
    text=True,
    encoding="utf-8"
    )
    return result.stdout

def main():
    video_id = input("Enter YouTube video ID: ").strip()
    transcript = get_transcript(video_id)
    if transcript:
        print("Transcript fetched, sending to local AI for summary...")
        summary = summarize_with_ollama(transcript)
        output_file = f"{video_id}_summary.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"Summary saved as {output_file}")
    else:
        print("Failed to fetch transcript.")

if __name__ == "__main__":
    main()
