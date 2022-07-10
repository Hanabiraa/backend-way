"""
Данный пример иллюстрирует реализации декораторов с их собственными аттрибутами,
 на основе как функции, так и класса
"""
import time


# реализация только функцией
def BenchmarkFunc(count=100):
    def _decorator(f):
        def _wrapper(*args, **kwargs):
            print(f'Function {f} testing by {BenchmarkFunc.__qualname__}')
            time_per_call = []
            for _ in range(count):
                t_start = time.perf_counter()
                f(*args, **kwargs)
                time_per_call.append(time.perf_counter() - t_start)
            print(f'Average time: {sum(time_per_call) / len(time_per_call)}')

        return _wrapper

    return _decorator


# реализация классом и функцией (можно наоборот, чтобы внешняя оболочка была функцией,
# а внутренняя - класс
class BenchmarkClass():
    def __init__(self, count=100):
        self.count = count

    def __call__(self, f):
        def _wrapper(*args, **kwargs):
            print(f'Function {f} testing by {BenchmarkClass.__call__.__qualname__}')
            time_per_call = []
            for _ in range(self.count):
                t_start = time.perf_counter()
                f(*args, **kwargs)
                time_per_call.append(time.perf_counter() - t_start)
            print(f'Average time: {sum(time_per_call) / len(time_per_call)}')

        return _wrapper


@BenchmarkFunc(count=1000)
def func1(nums, rank):
    _ = [x ** rank for x in range(nums)]


@BenchmarkClass(count=1000)
def func2(nums, rank):
    _ = [x ** rank for x in range(nums)]


if __name__ == '__main__':
    func1(1000, 4)
    func2(1000, 4)
