"""
Данный пример иллюстрирует пример создание декоратора для закрытых аттрибутов
"""


def private(*attrs):  # для сохранения атрибутов декоратора
    def onDecorator(cls):  # для сохранения callable объекта, что декорируем
        class Wrapper():
            def __init__(self, *args, **kwargs):
                self.obj = cls(*args, **kwargs)

            def __getattr__(self, item):
                if item in attrs:
                    raise AttributeError('Private attribute!')
                return getattr(self.obj, item)

            def __setattr__(self, item, value):
                if item == 'obj':
                    # необходимо для доступа экземпляра оболочки к своим атрибутам,
                    # иначе невозможно создание
                    self.__dict__[item] = value
                elif item in attrs:
                    raise AttributeError('Private attribute!')
                setattr(self.obj, item, value)

        return Wrapper

    return onDecorator


@private('age')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


if __name__ == '__main__':
    obj = Person('Bob', 25)
    obj.name = 'Mike'
    print(obj.get_age())
    print(obj.name)
    print(obj.age)
