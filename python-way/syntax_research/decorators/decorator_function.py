"""
Данный пример иллюстрирует простой декоратор на основе функций,
 который считает количество вызовов функции и возвращает ее результат
"""
import datetime


def tracer(f):
    call_counter = 0

    def _wrapper(*args, **kwargs):
        nonlocal call_counter
        call_counter += 1

        res = f(*args, **kwargs)
        print(f"Call func {f} {call_counter} times with value {res}")
        return res

    return _wrapper


@tracer
def f(fmt):
    return datetime.datetime.now().strftime(fmt)


if __name__ == '__main__':
    for _ in range(5):
        f('%H:%M:%S')
