from gtts import gTTS
import os
import uuid

class TTS:
    def __init__(self):
        pass

    def synthesize(self, text: str, language: str = "en") -> str:
        """Generate speech file from text"""
        filename = f"/tmp/{uuid.uuid4()}.mp3"
        tts = gTTS(text=text, lang=language)
        tts.save(filename)
        return filename
