"""
Пример простого метакласса с переопределением __new__ метакласса.
"""


class Meta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print('In meta..')
        print('clsname: ', clsname)
        print('superclasses: ', superclasses)
        print('attributedict: ', attributedict)
        return super().__new__(cls, clsname, superclasses, attributedict)


class Person():
    def __init__(self, name):
        self.name = name


class Worker(Person, metaclass=Meta):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position


if __name__ == '__main__':
    obj = Worker('Bob', 'DS')
