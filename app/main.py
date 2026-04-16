from dotenv import load_dotenv

from fastapi import FastAPI
from app.api.router import api_router

load_dotenv()

"""
Disable the automatic docs endpoints in production until needed. If needed internaly protect them behind auth
"""
app = FastAPI(title="VPS Agent",
              docs_url=None,
              redoc_url=None,
              openapi_url=None,
              )

app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"status": "ok"}
