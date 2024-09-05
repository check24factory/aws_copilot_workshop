import psutil
from fastapi import status, APIRouter

from api.data_models.v1.response import HealthResponse

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK, response_model=str, name='Health check of servers')
def health():
    return "OK"


@router.get("/info", status_code=status.HTTP_200_OK, response_model=HealthResponse, name='Info about the environment')
def info():
    return {
        "http_status_code": status.HTTP_200_OK,
        "health": "OK",
        "cpu_count": psutil.cpu_count(),
        "cpu_usage_relative": f"{psutil.cpu_percent()}%",
        "memory_usage_relative": f"{psutil.virtual_memory().percent}%",
        "memory_usage_absolute": f"{int(psutil.virtual_memory().used / 1024 / 1024)}Mb",
        "disk_usage": f"{psutil.disk_usage('/').percent}%",
    }
