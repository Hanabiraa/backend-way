FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /usr/src/

COPY ./src .