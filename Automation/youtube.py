from youtube_transcript_api import YouTubeTranscriptApi

video_id = "F2hN3JKZ-Go"
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    print(transcript)
except Exception as e:
    print(f"Error: {e}")
