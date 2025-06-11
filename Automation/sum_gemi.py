import subprocess
from youtube_transcript_api import YouTubeTranscriptApi
import os

OLLAMA_EXECUTABLE_PATH = r"C:\Users\gavsm\AppData\Local\Programs\Ollama\ollama.exe"
OLLAMA_MODEL = "llama3"

def get_video_id_from_input():
    while True:
        video_id = input("Enter YouTube video ID (e.g., dQw4w9WgXcQ): ").strip()
        if len(video_id) >= 11:
            return video_id
        else:
            print("Invalid video ID format. It's usually 11 characnwf-rVuCEkUters long. Please try again.")

def get_transcript(video_id):
    print(f"\nAttempting to fetch transcript for video ID: {video_id}...")
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        print(f"Successfully fetched {len(transcript_list)} transcript entries.")
        lines = [entry['text'] for entry in transcript_list]
        full_transcript = "\n".join(lines)
        return full_transcript
    except Exception as e:
        print(f"Error fetching transcript for {video_id}: {e}")
        return None

def save_transcript_to_file(transcript, video_id):
    filename = f"{video_id}_transcript.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(transcript)
        print(f"Transcript saved as: {filename}")
        return filename
    except Exception as e:
        print(f"Error saving transcript to file: {e}")
        return None

def load_transcript_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading transcript file: {e}")
        return None

def summarize_with_ollama(transcript_text, model_name=OLLAMA_MODEL):
    if not transcript_text:
        print("No transcript provided to summarize.")
        return None

    prompt = f"PLease summarise this in the tone and style of a northside Dublin Man from ireland who maons about the government. The conversation should be human-like and flow. --> {transcript_text} <--"

    try:
        ollama_command = [os.path.normpath(OLLAMA_EXECUTABLE_PATH), "run", model_name]
        result = subprocess.run(
            ollama_command,
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False
        )
        if result.returncode == 0:
            print("Summary received from Ollama.")
            return result.stdout.strip()
        else:
            print(f"Error communicating with Ollama:")
            print(f"Return Code: {result.returncode}")
            print(f"Stdout: {result.stdout}")
            print(f"Stderr: {result.stderr}")
            return None
    except FileNotFoundError:
        print(f"Error: The Ollama executable was not found at '{OLLAMA_EXECUTABLE_PATH}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while trying to run Ollama: {e}")
        return None

def save_summary_to_file(summary, video_id):
    output_filename = f"{video_id}_summary.txt"
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"Summary successfully saved as: {output_filename}")
    except Exception as e:
        print(f"Error saving summary to file: {e}")

def main():
    print("--- YouTube Transcript Summarizer (Transcript File Version) ---")

    video_id = get_video_id_from_input()
    transcript = get_transcript(video_id)
    if not transcript:
        print("Exiting due to failure in fetching transcript.")
        return

    # Step 1: Save transcript to file
    transcript_file = save_transcript_to_file(transcript, video_id)
    if not transcript_file:
        print("Exiting due to failure in saving transcript.")
        return

    # Step 2: Load transcript from file (guarantees what you read is what you have)
    transcript_from_file = load_transcript_from_file(transcript_file)
    if not transcript_from_file:
        print("Exiting due to failure in reading transcript from file.")
        return

    # Step 3: Summarize using transcript loaded from file
    summary = summarize_with_ollama(transcript_from_file)
    if summary:
        print("\n--- Summary ---")
        print(summary)
        save_summary_to_file(summary, video_id)
    else:
        print("Could not generate a summary.")

    print("\n--- Program Finished ---")

if __name__ == "__main__":
    main()

video_id = "--eVtP5oVcU"
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    print(transcript)
except Exception as e:
    print(f"Error: {e}")
