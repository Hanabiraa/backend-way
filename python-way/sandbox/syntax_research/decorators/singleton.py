"""
Реализация паттерна проектирования - singletom при помощи декоратора
"""


def singleton(cls):
    instance = None

    def _wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return _wrapper


@singleton
class Person:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    obj1 = Person('Bob')
    obj2 = Person('Mike')
    print(obj1.name, obj2.name)
    print(obj1, obj2)
    print(obj1 is obj1)
