from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="Resume–JD Alignment Scorer",
    version="1.0"
)

app.include_router(router)
