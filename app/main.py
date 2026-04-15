from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="VPS Agent")

app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"status": "ok"}
