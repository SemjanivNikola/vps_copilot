from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def services():
    return {"services_status": "OK"}
