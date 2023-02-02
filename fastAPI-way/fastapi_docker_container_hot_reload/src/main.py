from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "its correct work"}


"""
The server can be started locally with uvicorn src/main:app --reload and tested with curl -X GET http://localhost:8000.
Since we started the server with the --reload flag,
 modifying the return value of read_root will dynamically modify the return value from the http request.
"""
