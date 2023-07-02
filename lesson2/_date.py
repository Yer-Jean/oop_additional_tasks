"""Эта задача взята из урока 13.2 пункт 9
Задача со звездочкой №3:
Есть класс Date:
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

Реализуйте два метода from_string и is_date_valid. Метод from_string создает и инициализирует
экземпляр Date из переданной строки. Метод is_date_valid проверяет, корректные ли формат и
значение строки переданы."""
from datetime import datetime


# >>> date = Date.from_string('23-09-2022')
# >>> date.day
# 23
# >>> date.month
# 9
# >>> date.year
# 2022
# >>> Date.is_date_valid('23-09-2022')
# True
# >>> Date.is_date_valid('23-15-2022')  # месяц
# False
# >>> Date.is_date_valid('32-09-2022')  # день
# False

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, init_string):
        if Date.is_date_valid(init_string):
            day, month, year = init_string.split('-')
            return cls(int(day), int(month), int(year))
        else:
            print('Неправильная дата')
            return None

    @staticmethod
    def is_date_valid(init_string):
        try:
            datetime.strptime(init_string, "%d-%m-%Y")
            return True
        except ValueError:
            return False

date = Date.from_string('23-09-2022')
print(date)
print(date.day)
print(date.month)
print(date.year)
print(Date.is_date_valid('23-09-2022'))
print(Date.is_date_valid('23-15-2022'))
print(Date.is_date_valid('32-09-2022'))
date1 = Date.from_string('23-13-2022')
print(date1)

