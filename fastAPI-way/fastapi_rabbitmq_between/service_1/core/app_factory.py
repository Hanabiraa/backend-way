from fastapi import FastAPI, APIRouter

from service_1.api.api_v1.api import api_router
from service_1.core.config import get_settings, Settings

_settings: Settings = get_settings()


def create_app() -> FastAPI:
    app = FastAPI(
        title=_settings.service_title,
        redoc_url=None
    )

    # conf routers
    root_router = APIRouter()
    app.include_router(root_router)
    app.include_router(api_router, prefix=_settings.api_version, tags=["api"])
    return app
