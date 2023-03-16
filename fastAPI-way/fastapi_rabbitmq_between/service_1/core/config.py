import pathlib
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    service_title: str = "service 1"
    api_version: str = "/api/v1"
    project_root: pathlib.Path = pathlib.Path(__file__).resolve().parent

    # class Config:
    #     env_file = ".service_1.env"
    #     env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
