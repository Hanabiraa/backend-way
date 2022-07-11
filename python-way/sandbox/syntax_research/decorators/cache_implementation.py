"""
Пример реализации кэша посредством декоратора
"""

import collections
import time

class Cache():
    def __init__(self, size):
        self.hash_args = collections.OrderedDict()
        self.size = size

    def __call__(self, f):
        def _wrapper(*args, **kwargs):
            hash_key = self.__hash_args(*args, **kwargs)
            if hash_key not in self.hash_args:
                self.__update_hash_args(f, hash_key, *args, **kwargs)
            return self.hash_args[hash_key]

        return _wrapper

    @staticmethod
    def __hash_args(*args, **kwargs):
        return hash(str(*args) + str(**kwargs))

    def __update_hash_args(self, f, hash_key, *args, **kwargs):
        res = f(*args, **kwargs)
        self.hash_args[hash_key] = res
        if len(self.hash_args) > self.size:
            self.hash_args.popitem(last=False)


def recursiveFibSimple(n):
    if n == 1 or n == 2:
        return 1
    return recursiveFibSimple(n - 1) + recursiveFibSimple(n - 2)


@Cache(size=200)
def recursiveFibCache(n):
    if n == 1 or n == 2:
        return 1
    return recursiveFibCache(n - 1) + recursiveFibCache(n - 2)


if __name__ == '__main__':
    for func in [recursiveFibSimple, recursiveFibCache]:
        start_t = time.perf_counter()
        func(35)
        ellapsed = time.perf_counter() - start_t
        print(f'For func {func.__qualname__} computed time: {ellapsed} secs')
