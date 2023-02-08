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

    WS_MESSAGE_QUEUE: str = os.environ.get(
        "WS_MESSAGE_QUEUE", "redis://127.0.0.1:6379/0"
    )

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
