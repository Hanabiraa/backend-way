# Task custom decorator

As your code base grows, you may find that you're adding the same pieces of logic to all Celery tasks, like a custom retry strategy.

You can use Celery's Task decorator to abstract out such logic.

```python
class custom_celery_task:

    def __init__(self, *args, **kwargs):
        self.task_args = args
        self.task_kwargs = kwargs

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            # you can add custom code here
            return func(*args, **kwargs)

        task_func = shared_task(*self.task_args, **self.task_kwargs)(wrapper_func)
        return task_func
```

Very usefully link about class based decorator and functools.Decorator
https://tech.people-doc.com/python-class-based-decorators.html