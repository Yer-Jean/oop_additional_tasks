"""* Задача 2. Повышение производительности

В проекте имеется текущая реализация класса Person. Однако производительность программы, когда
создается большое количество экземпляров, низкая. Для повышения производительности предложите
свой подход к написанию класса, реализовав PersonTest.

Также для целей тестирования (код находится в функции main) реализуйте функцию get_set_delete,
которая работает с атрибутами обоих классов, т. е. делает различные манипуляции: читает данные
атрибута, присваивает новое значение атрибуту, удаляет атрибут.

Ознакомьтесь с кодом:

import timeit
from functools import partial

class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

class PersonTest:
    pass

def get_set_delete(person):
    pass

def main():
    person = Person("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    person_test = PersonTest("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    old = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    new = min(timeit.repeat(partial(get_set_delete, person_test), number=1000000))
    print(f"Текущая реализация: {old}")
    print(f"Тестовая реализация: {new}")
    print(f"Улучшение производительности: {(old - new) / old:.2%}")

if __name__ == "__main__":
    main()


Пример вывода при запуске кода:
Текущая реализация: 0.2782743
Тестовая реализация: 0.20101900000000006
Улучшение производительности: 27.76%
"""
import timeit
from functools import partial

class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

class PersonTest(Person):
    __slots__ = ('name', 'address', 'email')


def get_set_delete(person):
    person.name = 'Petr'
    person.address = 'hgjsvdchj'
    person.email = 'petr@mail.ru'
    _ = person.name
    __ = person.address
    ___ = person.email
    del person.name
    del person.address
    del person.email

def main():
    person = Person("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    person_test = PersonTest("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    old = min(timeit.repeat(partial(get_set_delete, person), number=1_000_000))
    new = min(timeit.repeat(partial(get_set_delete, person_test), number=1_000_000))
    print(f"Текущая реализация: {old}")
    print(f"Тестовая реализация: {new}")
    print(f"Улучшение производительности: {(old - new) / old:.2%}")

if __name__ == "__main__":
    main()
