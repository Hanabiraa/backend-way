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


class DevelopmentConfig(BaseConfig):
    ...


class Productionconfig(BaseConfig):
    ...


class TestingConfig(BaseConfig):
    ...


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


settings = get_settings()
