# api/routes_stt.py
from fastapi import APIRouter, UploadFile, Form
from stt.whisper_engine import WhisperSTT
import os

router = APIRouter()
stt_engine = WhisperSTT()

async def save_upload_to_tmp(file: UploadFile) -> str:
    tmp_path = f"/tmp/{file.filename}"
    with open(tmp_path, "wb") as f:
        f.write(await file.read())
    return tmp_path

@router.post("/stt/process")
async def process_audio(
    file: UploadFile,
    task: str = Form(...),  # "transcribe" or "translate"
    language: str = Form(None)  # optional
):
    tmp_path = await save_upload_to_tmp(file)

    try:
        if task == "transcribe":
            result = stt_engine.transcribe(tmp_path, language)
        elif task == "translate":
            result = stt_engine.translate(tmp_path, language)
        else:
            return {"error": "Invalid task. Use 'transcribe' or 'translate'."}
    finally:
        # cleanup temp file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return result
