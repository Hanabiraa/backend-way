# Multiple Queues and Task Routing

By default, Celery creates a default queue in your message broker when it's first executed. Celery then routes all tasks to that default queue and all Celery workers consume tasks from that queue as well. Celery allows you to spin up additional queues so you can have more control over which workers process which tasks.

> It's a good practice to configure at least one additional queue (two total) so you can route slow tasks to one queue and fast tasks to a different queue so that slow tasks don't block the fast tasks.


When u run the task - select queue:
```python
# enqueue task to the high_priority queue
divide.apply_async(args=[1, 2], queue='high_priority')

# enqueue task to the low_priority queue
divide.apply_async(args=[1, 2], queue='low_priority')
```

but dont forget tell worker which queue must be listened

## Task Routing

You can specify the destination for a particular task in the following places (in order of precedence):

1. Routing-related arguments in the apply_async method
2. Routing-related attributes on the Task
3. Routers defined in the CELERY_TASK_ROUTES setting 

It's a good practice to set some general rules in the CELERY_TASK_ROUTES and override them as necessary.

## Dynamic Routing
Instead of manually configuring routing rules per task, you can also configure the rules in CELERY_TASK_ROUTES dynamically.

To do this, let's first define a common naming convention for tasks:

```
<QUEUE>:<TASK_NAME>
```

in task:
```python
@shared_task(name="default:dynamic_example_one")
def dynamic_example_one():
    logger.info("Example One")


@shared_task(name="low_priority:dynamic_example_two")
def dynamic_example_two():
    logger.info("Example Two")
```

In config in CELERY_TASK_ROUTES
```python
def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "default"}

CELERY_TASK_ROUTES = (route_task,)
```

## Resources

Want to learn more? Check out the following resources:

1. [Routing Tasks](https://docs.celeryq.dev/en/stable/userguide/routing.html#basics)
2. [AMQP Primer](https://docs.celeryq.dev/en/stable/userguide/routing.html#id1)
3. [RabbitMQ Exchanges, routing keys and bindings](https://www.cloudamqp.com/blog/part4-rabbitmq-for-beginners-exchanges-routing-keys-bindings.html)