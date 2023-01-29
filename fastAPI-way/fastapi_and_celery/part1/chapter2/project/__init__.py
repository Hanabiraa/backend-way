from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI

    app.get(path="/")

    async def root():
        return {"message": "hello world!"}

    return app
