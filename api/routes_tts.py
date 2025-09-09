# api/routes_tts.py

from fastapi import APIRouter, Form
from fastapi.responses import FileResponse
from tts.gtts_engine import TTS

router = APIRouter()
tts_engine = TTS()

@router.post("/tts")
async def text_to_speech(text: str = Form(...), language: str = Form("en")):
    """
    Convert text to speech.
    Language can be 'en' (English) or 'hi' (Hindi).
    """
    audio_path = tts_engine.synthesize(text, language)
    return FileResponse(audio_path, media_type="audio/mpeg", filename="output.mp3")
