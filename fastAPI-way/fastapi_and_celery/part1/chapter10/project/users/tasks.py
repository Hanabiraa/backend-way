import random

import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from celery.signals import task_postrun
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

"""
Many resources on the web recommend using celery.task. 
This might cause circular imports since you'll have to import the Celery instance.
We used shared_task to make our code reusable,
which, again, requires current_app in create_celery instead of creating a new Celery instance.
Now, we can copy this file anywhere in the app and it will work as expected.
"""


@shared_task
def divide(x, y):
    # task debug
    # from celery.contrib import rdb
    # rdb.set_trace()

    import time
    time.sleep(7)
    return x / y


@shared_task()
def sample_task(email):
    from project.users.views import api_call

    api_call(email)


@shared_task(bind=True)
def task_process_notification(self):
    """
    Bound tasks are needed for retries (using app.Task.retry()),
    for accessing information about the current task request,
    and for any additional functionality you add to custom task base classes.

    Since we set bind to True, this is a bound task,
    so the first argument to the task will always be the current task instance (self).
    Because of this, we can call self.retry to retry the failed task.
    """
    try:
        if not random.choice([0, 1]):
            # mimic random error
            raise Exception()

        # this would block the I/O
        requests.post("https://httpbin.org/delay/5")
    except Exception as e:
        logger.error("exception raised, it would be retry after 5 seconds")
        raise self.retry(exc=e, countdown=5)


@task_postrun.connect
def task_postrun_handler(task_id, **kwargs):
    """
    We used async_to_sync to call update_celery_task_status (an asynchronous view) since,
    again, Celery does not work well with asyncio.
    """
    from project.ws.views import update_celery_task_status
    async_to_sync(update_celery_task_status)(task_id)

    from project.ws.views import update_celery_task_status_socketio
    # update_celery_task_status_socketio is a synchronous function, so we don't need to use async_to_sync.
    update_celery_task_status_socketio(task_id)


@shared_task(name="task_schedule_work")
def task_schedule_work():
    """
    We defined a name for the task via name="task_schedule_work".
    This name must be unique.
    """
    logger.info("task_schedule_work run")


@shared_task(name="default:dynamic_example_one")
def dynamic_example_one():
    logger.info("Example One")


@shared_task(name="low_priority:dynamic_example_two")
def dynamic_example_two():
    logger.info("Example Two")


@shared_task(name="high_priority:dynamic_example_three")
def dynamic_example_three():
    logger.info("Example Three")
