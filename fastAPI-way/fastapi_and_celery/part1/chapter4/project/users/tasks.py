from celery import shared_task

"""
Many resources on the web recommend using celery.task. 
This might cause circular imports since you'll have to import the Celery instance.
We used shared_task to make our code reusable,
which, again, requires current_app in create_celery instead of creating a new Celery instance.
Now, we can copy this file anywhere in the app and it will work as expected.
"""


@shared_task
def divide(x, y):
    import time

    time.sleep(7)
    return x / y
