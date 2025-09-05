# stt/whisper_engine.py
import whisper

class WhisperSTT:
    def __init__(self, model_size="small"):
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path: str, language: str = None):
        result = self.model.transcribe(audio_path, language=language)
        return {
            "transcript": result["text"],
            "language": result.get("language", language),

        }
