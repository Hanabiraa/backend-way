# Database Transactions

## What is it?

A database transaction is a unit of work that is either committed (applied to the database) or rolled back (undone from
the database) as a unit.

Most databases use the following pattern:

1. Begin the transaction.
2. Execute a set of data manipulations and/or queries.
3. If no error occurs, then commit the transaction.
4. If an error occurs, then roll back the transaction.

As you can see, a transaction is a very useful way to keep your data far away from chaos.

## Managing transactions

It's recommended to use the following pattern to wrap the database operation code:

```python
try:
    username = 'michael_test_1'
    user = User(
        username=f'{username}',
        email=f'{username}@test.com',
    )
    session.add(user)
    session.commit()
except Exception as e:
    session.rollback()
    raise
```

### **Do data reference to task, not the data**

In situations where a Celery task needs to work with data from a database, **you should always (if possible) enqueue a reference to the data rather than the data itself**. For example, rather than adding an email address, which could change before the task runs, add the user's primary database key.