# api/routes_stt.py
from fastapi import APIRouter, UploadFile, File, Form
from stt.whisper_engine import WhisperSTT
import tempfile

router = APIRouter()
stt_engine = WhisperSTT()

@router.post("/stt/transcribe")
async def transcribe(file: UploadFile = File(...), language: str = Form(None)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    result = stt_engine.transcribe(tmp_path, language)
    return result
