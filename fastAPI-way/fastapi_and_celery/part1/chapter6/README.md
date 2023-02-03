# Third-party Services

## Problem 1: Blocking Web Process

If you're running three Uvicorn workers with Gunicorn then you'll have three worker processes available to process each HTTP request to that entrypoint. If three users submit at the same time, all three processes might be blocked for at least five seconds.

Since requests is a synchronous library, one solution is to switch to a library that leverages asyncio, such as httpx or aiohttp. But in some cases, the third-party SDK is built without asyncio, so Celery is better option.

> Rather than introducing a polling mechanism (calling the API in a loop, checking the status of the task), you could use WebSockets or HTTP/2 to "push" the response from the server to the client after the task finishes executing. You'll see an example of this in the next chapter.

## Problem 2: Webhook Handler

Third party APIs often use webhooks to send event notifications. Depending on the notification, you may need to execute some sort of process. If the execution of this process is not handled in the background, this might block one of your Gunicorn workers until the process finishes execution.

# Conclusion

Be sure to handle third-party API calls appropriately in your applications as they can degrade performance. You can handle such calls asynchronously without Celery (using threads or asyncio, for example), but Celery can definitely simplify things if you have complicated logic / workflows associated with such third-party API calls.