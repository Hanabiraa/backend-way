# Deploy

1) In the entrypoint, we added a `rabbitmq_ready` function to check if RabbitMQ is up and running.
2) `exec "$@"` is used to make the entrypoint a "pass through" to ensure that Docker runs the command the user passes in (`command: /start`, in our case). For more, review this Stack Overflow answer https://stackoverflow.com/questions/39082768/what-does-set-e-and-exec-do-for-docker-entrypoint-scripts/39082923#39082923.

## about workers, when we use python-socketio

https://python-socketio.readthedocs.io/en/latest/server.html#eventlet-with-gunicorn

Based on the python-socketio docs, we set the worker number to 1.

Due to limitations in its load balancing algorithm, Gunicorn can only be used with one worker process, so the -w option cannot be set to a value higher than 1

## about main.py and project/asgi.py

1) In development mode, we'll still use main.py to serve up FastAPI and Celery, respectively.
2) In prod, both FastAPI and Celery will be served up via project/asgi.py.

