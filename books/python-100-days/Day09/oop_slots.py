# -*- coding: utf-8 -*-

class Person(object):

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('letterli', 12)
    person.play()
    person._gender = 'male'
    # person._address = 'gd' # AttributeError: 'Person' object has no attribute '_address'

if __name__ == '__main__':
    main()



