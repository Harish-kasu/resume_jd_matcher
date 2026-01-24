from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Resume–JD Alignment API")

app.include_router(router)

