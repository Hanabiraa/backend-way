import os
import pathlib
from functools import lru_cache
from typing import Any, Dict

from kombu import Queue  # Kombu is a messaging library that Celery leverages

"""
pydantic BaseSettings here bad choice, because
it might cause Celery to raise [ERROR/MainProcess] pidbox command error:
KeyError('__signature__') error when we launch Flower.
"""


def route_task(name, args, kwargs, options, task=None, **kw):
    """
    for dynamic task routing
    """
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "default"}


class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    DATABASE_URL: str = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3"
    )
    DATABASE_CONNECT_DICT: Dict[Any, Any] = {}

    CELERY_BROKER_URL: str = os.environ.get(
        "CELERY_BROKER_URL", "redis://127.0.0.1:6379/0"
    )

    # BROKER_USE_SSL: bool = True
    # CELERY_REDIS_BACKEND_USE_SSL: bool = True
    CELERY_RESULT_BACKEND: str = os.environ.get(
        "CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0"
    )

    CELERY_TASK_DEFAULT_QUEUE: str = "default"

    # Force all queues to be explicitly listed in `CELERY_TASK_QUEUES` to help prevent typos
    CELERY_TASK_CREATE_MISSING_QUEUES: bool = False

    CELERY_TASK_QUEUES: list = (
        # need to define default queue here or exception would be raised
        Queue("default"),
        Queue("high_priority"),
        Queue("low_priority"),
    )

    """
    So, all tasks with a name that matches project.users.tasks.* are routed to the high_priority queue.
    Tasks that do not match that pattern will be routed to the default queue. 
    """
    # CELERY_TASK_ROUTES = {
    #     "project.users.tasks.*": {
    #         "queue": "high_priority",
    #     },
    # }
    CELERY_TASK_ROUTES = (route_task,)  # for dynamic routs

    """
    Celery 's method for prefetching is not very efficient, both dynamically and globally.
    It can actually cause problems quite often. We recommend limiting prefetching to one
    so that each worker gets only one message at a time:
    """
    CELERY_WORKER_PREFETCH_MULTIPLIER = 1

    CELERY_TASK_ACKS_LATE = True

    """
    Celery workers send an acknowledgement back to the message broker after a task is picked up from the queue.
    The broker will usually respond by removing the task from the queue.
    This can cause problems if the worker dies while running the task and the task has been removed from the queue.

    To address this, you can configure the message broker to only acknowledge tasks
    (and subsequently remove the task from the queue) after the tasks have completed (succeeded or failed):
    """
    WS_MESSAGE_QUEUE: str = os.environ.get(
        "WS_MESSAGE_QUEUE", "redis://127.0.0.1:6379/0"
    )

    """
    To prevent tasks from hanging, you can set a soft or hard time limit globally or
    per task when you define or call the task:
    
    # per task when defined
    @celery.task(time_limit=30, soft_time_limit=10)
    def your_task():
        try:
            return do_something()
        except SoftTimeLimitExceeded:
            cleanup_in_a_hurry()
    
    # per task when called
    your_task.apply_async(args=[], kwargs={}, time_limit=30, soft_time_limit=10)
    
    or globally
    """
    CELERY_TASK_SOFT_TIME_LIMIT = 15 * 60
    CELERY_TASK_TIME_LIMIT = CELERY_TASK_SOFT_TIME_LIMIT + 30

    """
    Everything passed into Celery is serialized and everything that comes out is deserialized.
    Because of this, it's recommended to force developers into good practices for task arguments by
    setting task_serializer to json:
    """
    CELERY_TASK_SERIALIZER = "json"

    CELERY_BEAT_SCHEDULE: dict = {
        # "task-schedule-work": {
        #     "task": "task_schedule_work", # The task field is the task name
        #     "schedule": 5.0, # 5 seconds, The schedule field supports crontab, timedelta, and solar formats.
        # }
    }

    UPLOADS_DEFAULT_DEST: str = str(BASE_DIR / "upload")


class DevelopmentConfig(BaseConfig):
    """
    tasks will be executed immediately (synchronously) instead of being sent to the queue (asynchronously),
    allowing you to debug the code within the task as you normally would
    (with breakpoints and print statements and what not) with any other code in your FastAPI app
    """

    CELERY_TASK_ALWAYS_EAGER: bool = False


class Productionconfig(BaseConfig):
    ...


class TestingConfig(BaseConfig):
    CELERY_TASK_ALWAYS_EAGER: bool = True

    # https://fastapi.tiangolo.com/advanced/testing-database/
    DATABASE_URL: str = "sqlite:///./test.db"
    DATABASE_CONNECT_DICT: dict = {"check_same_thread": False}


@lru_cache
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": Productionconfig,
        "testing": TestingConfig,
    }

    config_name = os.environ.get("FASTAPI_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings: DevelopmentConfig | Productionconfig | TestingConfig = get_settings()
