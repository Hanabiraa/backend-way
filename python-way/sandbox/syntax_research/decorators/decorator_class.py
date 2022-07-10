"""
Данный пример иллюстрирует простой декоратор на основе класса,
 который считает количество вызовов функции и возвращает ее результат
"""
import datetime


class Tracer():
    def __init__(self, f):
        self.f = f
        self.call_counter = 0

    def __call__(self, *args, **kwargs):
        self.call_counter += 1
        res = self.f(*args, *kwargs)
        print(f"Call func {f} {self.call_counter} times with value {res}")
        return res


@Tracer
def f(fmt):
    return datetime.datetime.now().strftime(fmt)


if __name__ == '__main__':
    for _ in range(5):
        f('%H:%M:%S')
