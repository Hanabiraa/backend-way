"""
Данный пример показывает, как можно реализовать дескриптор данных property с дескрипторным синтаксисом
"""


class Property():
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __set_name__(self, owner, name):
        self.attr = name

    def __get__(self, instance, owner):
        if not self.fget:
            raise AttributeError
        return self.fget(instance)

    def __set__(self, instance, value):
        if not self.fset:
            object.__setattr__(instance, self.attr, value)
            return
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class Person:
    """
    property с синтаксисом дескриптора
    """

    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        print(f"{Person.get_name.__qualname__} called")
        return self._name

    def set_name(self, name):
        print(f"{Person.set_name.__qualname__} called")
        self._name = name

    def del_name(self):
        print(f"{Person.del_name.__qualname__} called")
        del self._name

    name = Property(
        fget=get_name,
        fset=set_name,
        fdel=del_name,
        doc="this is property")


if __name__ == '__main__':
    print('Create instance property')
    obj = Person('bob')
    print('property get option:')
    print(obj.name)

    print('\nproperty set option:')
    obj.name = 'Mike'
    print(obj.name)

    print('\nproperty del option:')
    del obj.name
