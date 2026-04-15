from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def metrics():
    return {"metics_status": "OK"}
