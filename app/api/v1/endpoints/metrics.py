from fastapi import APIRouter
from app.services.system_services import get_system_metrics

router = APIRouter()


@router.get('/')
def metrics():
    return get_system_metrics()
