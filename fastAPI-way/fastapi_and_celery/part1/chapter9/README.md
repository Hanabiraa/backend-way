# Celery beat and periodic tasks

The schedule field supports crontab, timedelta, and solar formats.

You can see a full list of configurable fields for CELERY_BEAT_SCHEDULE [here](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#available-fields).

## Dynamic Config

What if you need to add, edit, or remove a periodic task dynamically? In other words, what if you wanted to make a change to the config at runtime? Check out the following projects:

1. [redisbeat](https://github.com/liuliqiang/redisbeat)
2. [celery-sqlalchemy-scheduler](https://github.com/AngelLiang/celery-sqlalchemy-scheduler)