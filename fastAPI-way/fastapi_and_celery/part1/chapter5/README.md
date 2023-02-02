# Debugging a Celery Task

## Method 1: Eager Mode

By setting task_always_eager to True, tasks will be executed immediately (synchronously) instead of being sent to the queue (asynchronously), allowing you to debug the code within the task as you normally would (with breakpoints and print statements and what not) with any other code in your FastAPI app.

**This mode is recommended for use during testing as well**

### Pros 
You don't need to run the worker, message broker, or result backend processes to debug your code. In other words, you can debug the code within the Uvicorn server process directly. This greatly simplifies both debugging and testing.

### Cons
With this mode active, task.delay() returns EagerResult instead of AsyncResult, which could mask the actual problem.

## Methods 2: rdb

**rdb** is a powerful tool that allows you to debug your Celery task directly in your terminal.

You must have Telnet installed in order for this to work. Task must be async (task eager mode = false)

### Pros
You can debug the Celery task in an efficient way without an IDE.

### Cons
It can be difficult for beginners.

in dockerfile add new deps - 

```shell
apt install telnet
```

add in task code, which u want to debug this:
```python
from celery.contrib import rdb
rdb.set_trace()
```

then run docker compose and start to check logs by the command:
```sh
docker compose logs -f
```

in logs find this message:

```text
chapter5-celery_worker-1  | [2023-02-02 19:23:51,391: INFO/MainProcess] Task project.users.tasks.divide[10442fe6-d581-449e-9e72-4b8400a24937] received
chapter5-celery_worker-1  | [2023-02-02 19:23:51,436: WARNING/ForkPoolWorker-4] Remote Debugger:6903: Ready to connect: telnet 127.0.0.1 6903
chapter5-celery_worker-1  | 
chapter5-celery_worker-1  | Type `exit` in session to continue.
chapter5-celery_worker-1  | 
chapter5-celery_worker-1  | Remote Debugger:6903: Waiting for client...
```

in other terminal connect to debugger by **telnet** (find this message in logs)

and start debug

```text
(Pdb) args
x = 1
y = 2

(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    cl         display   j         next     run     unalias    where
a      clear      down      jump      p        rv      undisplay
alias  commands   enable    l         pp       s       unt
args   condition  h         list      r        source  until
b      d          help      ll        restart  step    up
break  debug      ignore    longlist  return   tbreak  w
bt     disable    interact  n         retval   u       whatis

Miscellaneous help topics:
==========================
exec  pdb

Undocumented commands:
======================
c  cont  continue  exit  q  quit
```