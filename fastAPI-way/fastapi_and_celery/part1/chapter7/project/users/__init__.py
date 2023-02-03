from fastapi import APIRouter

users_router = APIRouter(
    prefix="/users",
)

# (circular import, if place in beginning)
from . import models, tasks, views # noqa

