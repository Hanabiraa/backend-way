# Pytest

The key to writing test cases for Celery tasks is to **test Celery tasks like normal Python functions**. In other words, don't worry about testing whether or not the tasks are run synchronously or asynchronously since this is a Celery feature (you should assume that the Celery developers are testing this accordingly).