from fastapi import FastAPI

from project.celery_utils import create_celery


def create_app() -> FastAPI:
    app = FastAPI()

    # do it before load routes
    app.celery_app = create_celery()

    from project.users import users_router

    app.include_router(users_router)

    @app.get("/")
    async def root():
        return {"message": "Hello world"}

    return app
