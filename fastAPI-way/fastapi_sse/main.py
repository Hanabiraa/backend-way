import asyncio
import uvicorn
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


STREAM_DELAY = 1  # second
RETRY_TIMEOUT = 15000  # milisecond


@app.get('/stream')
async def message_stream(request: Request):
    def new_messages():
        # Add logic here to check for new messages
        yield 'Hello World'

    async def event_generator():
        while True:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            # Checks for new messages and return them to client if any
            if new_messages():
                yield {
                    "event": "new_message",
                    "id": "message_id",
                    "retry": RETRY_TIMEOUT,
                    "data": "message_content"
                }

            await asyncio.sleep(STREAM_DELAY)

    return EventSourceResponse(event_generator())
