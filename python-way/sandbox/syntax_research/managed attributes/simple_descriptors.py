"""
Пример реализации дескриптора данных и дескриптора не данных.
Данный пример показывает различия в приоритете дескриптора при поиске аттрибута в экземпляре класса
"""


class DataDescriptor():
    def __set_name__(self, owner, name):
        print(f"{self.__class__.__name__} __set_name__")
        self.cls = owner
        self.attr = name

    def __get__(self, instance, owner):
        print(f"{self.__class__.__name__} __get__")
        return instance.__dict__[self.attr]

    def __set__(self, instance, value):
        print(f"{self.__class__.__name__} __set__")
        instance.__dict__[self.attr] = value


class NonDataDescriptor():
    def __set_name__(self, owner, name):
        print(f"{self.__class__.__name__} __set_name__")
        self.cls = owner
        self.attr = name

    def __get__(self, instance, owner):
        print(f"{self.__class__.__name__} __get__")
        return instance.__dict__[self.attr]


class Person:
    name = DataDescriptor()
    age = NonDataDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    print('\nCreate Person object')
    obj = Person('Mike', 20)

    print('\nTest Data descriptor')
    _ = obj.name
    obj.name = 'Bob'

    print('\nTest Non-data descriptor')
    _ = obj.age
    obj.age = 41
    _ = obj.age