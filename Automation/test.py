#!/usr/bin/env python3
"""
Quick ‘n’ dirty Gemini TTS tester.
"""

import wave
from google import genai
from google.genai import types

# 💀 Replace with your real API key
API_KEY = "AIzaSyCN-HZPF7m1bZRkhaP9NRvC9JTPMUp9CjI"

# Helper: save PCM bytes to .wav
def save_wav(filename: str, pcm_bytes: bytes, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm_bytes)
    print(f"Saved: {filename}")

def single_speaker_tts(text: str, voice_name: str = "Kore"):
    client = genai.Client(api_key=API_KEY)
    resp = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice_name)
                )
            ),
        ),
    )
    pcm = resp.candidates[0].content.parts[0].inline_data.data
    save_wav("single_speaker.wav", pcm)

def multi_speaker_tts(conversation: str, speakers: dict):
    """
    conversation: e.g.
      "Joe: Hey Jane, how's tricks?\nJane: Grand, yerself?"
    speakers: {
      "Joe": "Kore",
      "Jane": "Puck"
    }
    """
    client = genai.Client(api_key=API_KEY)
    # build speaker configs
    configs = []
    for name, voice in speakers.items():
        configs.append(types.SpeakerVoiceConfig(
            speaker=name,
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
            )
        ))
    resp = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=conversation,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=configs
                )
            ),
        ),
    )
    pcm = resp.candidates[0].content.parts[0].inline_data.data
    save_wav("multi_speaker.wav", pcm)

if __name__ == "__main__":
    # Test single speaker
    single_speaker_tts(
        "Say cheerfully: Have a wonderful day!",
        voice_name="Kore"
    )

    # Test multi-speaker
    convo = """Joe: How's it going today, Jane?
Jane: Not too bad, how about you?"""
    multi_speaker_tts(convo, {"Joe": "Kore", "Jane": "Puck"})
