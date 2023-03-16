from fastapi import APIRouter

from service_1.api.api_v1.endpoints import tasks

api_router = APIRouter()
api_router.include_router(router=tasks.router, prefix="/task", tags=["task"])
