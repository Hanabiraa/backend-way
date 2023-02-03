import os
import pathlib
from functools import lru_cache
from typing import Any, Dict

"""
pydantic BaseSettings here bad choice, because
it might cause Celery to raise [ERROR/MainProcess] pidbox command error:
KeyError('__signature__') error when we launch Flower.
"""


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
    # CELERY_TASK_ALWAYS_EAGER: bool = True
    CELERY_TASK_ALWAYS_EAGER: bool = False


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
