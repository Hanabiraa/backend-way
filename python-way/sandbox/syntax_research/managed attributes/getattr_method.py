"""
Данный пример иллюстрирует применение метода __getattr__ для управления атрибутами
"""


class CheckWrapper():
    def __init__(self, cls, *args, **kwargs):
        self.cls = cls(*args, **kwargs)

    def __getattr__(self, item):
        """
        Трассировка доступа к атрибуту
        """
        print(f'{CheckWrapper.__getattr__.__qualname__} call: {item}')

        if not hasattr(self.cls, item):
            raise AttributeError

        # Можно выбрать между
        # return self.cls.__dict__[item]
        # return getattr(self.cls, item)
        return object.__getattribute__(self.cls, item)

class Info():
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    print('Create instance')
    obj = CheckWrapper(Info, 12)

    print('Testing getattr method: ')
    print(obj.value)
    print('Testing setattr method: ')
    obj.value = 44

    print('Wrapper: ', obj.__dict__)
    print('cls: ', obj.cls.__dict__)
