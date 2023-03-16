from fastapi import APIRouter, status

router = APIRouter()

successful_tasks = 0

@router.get(
    "/GetStats",
    status_code=status.HTTP_200_OK,
    summary="Return number of successfully task"
)
def get_number_of_successfully_task():
    global successful_tasks
    return successful_tasks
