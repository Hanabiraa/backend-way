# Retrying Failed Tasks

1. **try/except block**

    Since we set bind to True, this is a bound task, so the first argument to the task will always be the current task instance (self). Because of this, we can call self.retry to retry the failed task.
    
    Please remember to raise the exception returned by the self.retry method to make it work.
2. **Task Retry Decorator**

   * *autoretry_for* arg takes a list/tuple of exception types that you'd like to retry for.

   * *retry_kwargs* takes a dictionary of additional options for specifying how autoretries are executed

   ```python
   @shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 7, "countdown": 5})
   def task_process_notification(self):
       if not random.choice([0, 1]):
           # mimic random error
           raise Exception()

    requests.post("https://httpbin.org/delay/5")
   ```

3. **Exponential Backoff**

   If your Celery task needs to send a request to a third-party service, it's a good idea to use exponential backoff to avoid overwhelming the service.
   
   ```python
   @shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5})
   def task_process_notification(self):
       if not random.choice([0, 1]):
           # mimic random error
           raise Exception()

    requests.post("https://httpbin.org/delay/5")
   ```
   
   ```text
   celery_worker_1  | [2022-08-28 14:09:19,043: INFO/ForkPoolWorker-2] Task project.users.tasks.task_process_notification[4bbfee67-6ce6-4225-a172-e4b1152afc89] retry: Retry in 1s: Exception()
   celery_worker_1  | [2022-08-28 14:09:20,101: INFO/ForkPoolWorker-2] Task project.users.tasks.task_process_notification[4bbfee67-6ce6-4225-a172-e4b1152afc89] retry: Retry in 2s: Exception()
   celery_worker_1  | [2022-08-28 14:09:22,156: INFO/ForkPoolWorker-2] Task project.users.tasks.task_process_notification[4bbfee67-6ce6-4225-a172-e4b1152afc89] retry: Retry in 4s: Exception()
   celery_worker_1  | [2022-08-28 14:09:26,246: INFO/ForkPoolWorker-2] Task project.users.tasks.task_process_notification[4bbfee67-6ce6-4225-a172-e4b1152afc89] retry: Retry in 2s: Exception()
   celery_worker_1  | [2022-08-28 14:09:28,355: INFO/ForkPoolWorker-2] Task project.users.tasks.task_process_notification[4bbfee67-6ce6-4225-a172-e4b1152afc89] retry: Retry in 1s: Exception()
   ```
   
   You can also set retry_backoff to a number for use as a delay factor:

4. **Task Base Class**

   If you find yourself writing the same retry arguments in your Celery task decorators, you can (as of Celery 4.4) define retry arguments in a base class, which you can then use as a base class in your Celery tasks

   ```python
   class BaseTaskWithRetry(celery.Task):
   autoretry_for = (Exception, KeyError)
   retry_kwargs = {"max_retries": 5}
   retry_backoff = True


   @shared_task(bind=True, base=BaseTaskWithRetry)
   def task_process_notification(self):
       raise Exception()
   ```


# Bonus

When you build a custom retry strategy for your Celery task (which needs to send a request to another service), you should add some randomness to the delay calculation to prevent all tasks from being executed simultaneously resulting in a [thundering herd](https://en.wikipedia.org/wiki/Thundering_herd_problem).

Celery has you covered here as well with retry_jitter
```python
@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_jitter=True, retry_kwargs={"max_retries": 5})
def task_process_notification(self):
```
**This option is set to True by default,** which helps prevent the thundering herd problem when you use Celery's built-in retry_backoff.
