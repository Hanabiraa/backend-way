"""
Данный пример иллюстрирует дескриптор данных с сохранением своего состояния
между вызовами
"""


class DescState:
    def __init__(self, label: str):
        self.label = label

    def __set_name__(self, owner, name):
        self.attr = name

    def __get__(self, instance, owner):
        print(self.label, DescState.__get__.__qualname__)
        return instance.__dict__[self.attr]

    def __set__(self, instance, value):
        print(self.label, DescState.__set__.__qualname__)
        instance.__dict__[self.attr] = value


class Person:
    name = DescState('Person.name: ')
    age = DescState('Person.age: ')


if __name__ == '__main__':
    print('Create instance')
    obj = Person()
    print('Instance dict: ', obj.__dict__)

    print('Test __set__')
    obj.name = 'Bob'
    obj.age = 45

    print('Test __get__')
    _ = obj.name
    _ = obj.age

    print('Instance dict: ', obj.__dict__)
