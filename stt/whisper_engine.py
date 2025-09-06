# stt/whisper_engine.py
import whisper

class WhisperSTT:
    def __init__(self, model_size="small"):
        self.model = whisper.load_model(model_size)

    def _process_audio(self, audio_path: str, language: str = None, task: str = "transcribe"):
        """
        Internal helper to handle both transcription and translation.
        """
        if language:
            # Forced language (skip detection)
            result = self.model.transcribe(audio_path, language=language, task=task)
            return {
                "language": language,
                task: result["text"].strip()
            }
        else:
            # Auto-detect language first
            audio = whisper.load_audio(audio_path)
            audio = whisper.pad_or_trim(audio)
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

            _, probs = self.model.detect_language(mel)
            detected_language = max(probs, key=probs.get)
            confidence = float(probs[detected_language])

            result = self.model.transcribe(audio_path, language=detected_language, task=task)

            return {
                "detected_language": detected_language,
                "confidence": confidence,
                task: result["text"].strip()
            }

    def transcribe(self, audio_path: str, language: str = None):
        return self._process_audio(audio_path, language, task="transcribe")

    def translate(self, audio_path: str, language: str = None):
        return self._process_audio(audio_path, language, task="translate")
