# Logging

## Logging FastAPI

To learn more about logging, check out [Python's Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html).

## Logging Celery tasks

Celery have func -> `get_task_logger`
[Link to docs](https://docs.celeryq.dev/en/stable/userguide/tasks.html#logging)

```python
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y
```

## Custom celery task logging

You can use the Celery `after_setup_logger` and `after_setup_task_logger` signals, which are sent after Celery sets up the logger, to modify the logger.

> This is recommended method in most cases since it's the least invasive.

```python
import logging

from celery.signals import after_setup_logger

@after_setup_logger.connect()
def on_after_setup_logger(logger, **kwargs):
    formatter = logger.handlers[0].formatter
    file_handler = logging.FileHandler('celery.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
```

You should now be able to see all Celery task logs in celery.log.


