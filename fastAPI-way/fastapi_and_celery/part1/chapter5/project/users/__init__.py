from fastapi import APIRouter
from . import models, tasks

user_router = APIRouter(
    prefix="/users",
)
