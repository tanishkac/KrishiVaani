# api/main.py
from fastapi import FastAPI
from api.routes_stt import router as stt_router

app = FastAPI(title="KrishiVaani - STT Service")
app.include_router(stt_router)
