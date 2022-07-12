"""
Данный пример иллюстририует использование декораторов для динамических атрибутов
"""
import datetime


class DescDate():
    def __get__(self, instance, owner):
        print(f'{DescDate.__get__.__qualname__} call')
        return datetime.datetime.now()


class SomeInfo:
    time = DescDate()


if __name__ == '__main__':
    print('Create instance')
    obj = SomeInfo()
    print(obj.time)