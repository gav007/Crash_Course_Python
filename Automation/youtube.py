from youtube_transcript_api import YouTubeTranscriptApi

# Replace with your video ID (the part after "v=" in the URL)
video_id = "nwf-rVuCEkU"

# Fetch the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Convert to plain text
lines = [entry['text'] for entry in transcript]
full_transcript = "\n".join(lines)

# Save to file
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(full_transcript)

print("Transcript saved as transcript.txt")
