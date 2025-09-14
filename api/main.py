# api/main.py
from fastapi import FastAPI
from api.routes_stt import router as stt_router
from api.routes_tts import router as tts_router
from api.routes_chat import router as chat_router


app = FastAPI(title="KrishiVaani - STT Service + TTS Service")
app.include_router(stt_router)
app.include_router(tts_router)
app.include_router(chat_router, prefix="/chat", tags=["Chat / NLU"])