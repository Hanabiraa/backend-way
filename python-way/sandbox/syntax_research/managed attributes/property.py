"""
Данный пример иллюстрирует применение property как с помощью декоративного синтаксиса,
так и как дескриптор

property - дескриптор данных
"""


class Person_desc:
    """
    property с синтаксисом дескриптора
    """

    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        print(f"{Person_desc.get_name.__qualname__} called")
        return self._name

    def set_name(self, name):
        print(f"{Person_desc.set_name.__qualname__} called")
        self._name = name

    def del_name(self):
        print(f"{Person_desc.del_name.__qualname__} called")
        del self._name

    name = property(
        fget=get_name,
        fset=set_name,
        fdel=del_name,
        doc="this is property")

class Person_dec:
    """
    property с синтаксисом декоратора
    """

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        """
        this is property
        """
        print(f"{Person_desc.get_name.__qualname__} called")
        return self._name

    @name.setter
    def name(self, name):
        print(f"{Person_desc.set_name.__qualname__} called")
        self._name = name

    @name.deleter
    def name(self):
        print(f"{Person_desc.del_name.__qualname__} called")
        del self._name


if __name__ == '__main__':
    for cls, type in zip([Person_desc, Person_dec], ['descriptor syntax', 'decorator syntax']):
        print(f'Create instance property {type}')
        obj = cls('bob')
        print('property get option:')
        print(obj.name)

        print('\nproperty set option:')
        obj.name = 'Mike'

        print('\nproperty del option:')
        del obj.name

        print('\nproperty doc option:')
        print(Person_desc.name.__doc__, end='\n\n')