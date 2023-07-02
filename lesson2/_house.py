"""Эта задача взята из урока 13.2 пункт 9
Задача со звездочкой №2:

Реализуйте класс House с одним защищенным атрибутом — цена. Добейтесь поведения от этого класса
описанного в теле модуля ниже"""
# >>> house = House(50000.0)
#
# >>> house.price
# 50000.0
#
# >>> house.price = 45000.0  # обновили значение
# >>> house.price
# 45000.0
#
# >>> house.price = -50
# Пожалуйста, введите корректное значение
#
# >>> house.price
# 45000.0
#
# >>> del house.price
# >>> house.price
# AttributeError: 'House' object has no attribute '_price'.

class House:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print('Пожалуйста, введите корректное значение')

    @price.deleter
    def price(self):
        del self.__price


house = House(50000.0)
print(house.price)  # 50000.0

house.price = 45000.0
print(house.price)  # 45000.0

house.price = -50   # Пожалуйста, введите корректное значение
print(house.price)  # 45000.0

del house.price
print(house.price)  # AttributeError: 'House' object has no attribute '_price'

