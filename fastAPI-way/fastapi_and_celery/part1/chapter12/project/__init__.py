from broadcaster import Broadcast
from fastapi import FastAPI

from project.config import settings

"""
We created a new instance of Broadcast, which will be only used by FastAPI, not the Celery worker.
"""
broadcast = Broadcast(settings.WS_MESSAGE_QUEUE)


def create_app() -> FastAPI:
    app = FastAPI()

    # do it before load routes
    from project.celery_utils import create_celery
    app.celery_app = create_celery()

    from project.users import users_router
    app.include_router(users_router)

    from project.ws import ws_router
    app.include_router(ws_router)

    from project.ws.views import register_socketio_app
    register_socketio_app(app)

    @app.on_event("startup")
    async def startup_event():
        """
        In the startup event handler we established the connection while in shutdown we disconnected from it.
        """
        await broadcast.connect()

    @app.on_event("shutdown")
    async def shutdown_event():
        await broadcast.disconnect()

    @app.get("/")
    async def root():
        return {"message": "Hello world"}

    return app
