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
        "Say cheerfully: Have a Fecking wonderful day!",
        voice_name="Kore"
    )

    # Test multi-speaker
    convo = """Sgt. O’Reilly:3
Right Joe, let’s not mess about. You know why you’re here.

Joe:
Yeah — ‘cos me neighbour’s a rat and your lad outside couldn’t tell the difference between a grow lamp and a lava lamp.

Garda McDonagh:
You were spotted leggin' it out of Lidl with two trolleys full of bacon rashers and twenty packets of Daz. Care to explain that one?

Joe:
It was a spiritual emergency. I was makin’ a breakfast bap for the ages.

Sgt. O’Reilly:
You pushed an old lad into the freezer aisle, Joe.

Joe:
He was blockin’ the puddin’. That’s practically assault on me heritage.

Garda McDonagh:
And the week before, CCTV caught ya tryin’ to hotwire a Garda van with a curly straw.

Joe:
Yeah, and if ye didn’t cheap out on ignition systems I’d have been in Galway by lunch.

Sgt. O’Reilly:
Don’t get smart, ya little bollix.

Joe:
Can’t help it — every time I’m in here, I gain IQ points from listenin’ to this interrogation technique ye stole from Father Ted reruns.

Garda McDonagh:
We also found a pigeon in your hoodie, Joe. A live pigeon. Why?

Joe:
Emotional support bird. Name’s Declan. He’s got anxiety and a vendetta against Luas inspectors.

Sgt. O’Reilly:
You think this is a joke? We’ve got twenty witnesses sayin’ you started a conga line in the dole office shoutin’ “UP THE RA FOR RENT FREE LIVING!”

Joe:
That’s not a crime, that’s community engagement. And to be fair, the rhythm was immaculate.

Garda McDonagh:
Right, that’s enough. Last chance — you plead guilty or we show the judge the footage of you doin’ karaoke in Supermacs at 2am with a traffic cone on your head.

Joe:
Ah, shite. Alright, guilty on the rashers. But Declan walks free. He’s innocent. And he’s got court anxiety.

[Scene ends with Declan the pigeon shitting on Sgt. O’Reilly’s notebook and Joe gettin’ a three-week community service order — cleanin’ pigeon droppings off Ballymun bus stops.]"""
    multi_speaker_tts(convo, {"Joe": "Kore", "Jane": "Puck"})
