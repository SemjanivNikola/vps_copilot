from fastapi import FastAPI
from app.api.router import api_router
from dotenv import load_dotenv
from slowapi import Limiter
from slowapi.util import get_remote_address

load_dotenv()
limiter = Limiter(key_func=get_remote_address)

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
@limiter.limit("5/minute")
def root():
    return {"status": "ok"}
