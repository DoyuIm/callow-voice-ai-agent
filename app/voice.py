from gtts import gTTS
import whisper
import os

whisper_model = whisper.load_model("base")


def speech_to_text(audio_path: str) -> str:
    result = whisper_model.transcribe(audio_path)
    return result["text"]


def text_to_speech(text: str, output_path: str = "output.mp3") -> str:
    tts = gTTS(text=text, lang="ko")
    tts.save(output_path)
    return output_path