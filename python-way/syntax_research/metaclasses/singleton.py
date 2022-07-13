"""
Пример реализации паттерна синглтон при помощи метакласса
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print('On call..', cls)
        if cls not in Singleton._instances:
            Singleton._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return Singleton._instances[cls]


class SingletonNumCls(metaclass=Singleton):
    def __init__(self, num):
        self.num = num


class SingletonStrCls(metaclass=Singleton):
    def __init__(self, str):
        self.str = str


if __name__ == '__main__':
    num1 = SingletonNumCls(1)
    num2 = SingletonNumCls(2)
    str1 = SingletonStrCls('Bob')
    str2 = SingletonStrCls('Mike')

    print(num1, num2)
    print(num1.num, num2.num)
    print(num1 is num2)
    print(str1, str2)
    print(str1.str, str2.str)
    print(str1 is str2)
