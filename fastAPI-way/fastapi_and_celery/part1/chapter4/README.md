Live code reloading is a simple yet effective way for developers to get quick feedback on code changes. While Uvicorn provides this functionality out-of-the-box, Celery does not. So, you'll have to manually restart the workers every time you make code changes to a task, which can make for a very difficult developer experience.

**watchfiles solve this problem**, a tool used for file watching and code reload

see *compose/local/fastapi/celery/worker/start*