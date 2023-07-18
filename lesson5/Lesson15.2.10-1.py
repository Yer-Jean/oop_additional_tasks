"""Задача 1. Логгер магических методов. Функция super()
Создайте класс MyList, который наследуется от встроенного класс list и полностью ведет себя как list.

class MyList(list):
    pass

Однако работа некоторых его магических методов логируется выводом в консоль сообщения "Работает магический метод".
Подумайте, какие магические методы надо расширить, чтобы в результате работы следующего кода в консоль вывелось
не менее 5 сообщений о работе магических методов.

Код:

lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))

Вывод в консоль:

Работает магический метод
Работает магический метод
Работает магический метод
Работает магический метод
['Jone', 'Snow', 'Python']
Работает магический метод
3
"""

class MyList(list):

    def __new__(cls, *args, **kwargs):
        print('Работает магический метод new')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, data_list):
        super().__init__(data_list)
        # self.data_list = data_list
        print('Работает магический метод init')

    def __getitem__(self, item):
        print('Работает магический метод getitem')
        # return self.data_list[item]
        return super().__getitem__(item)

    def __setitem__(self, item, value):
        print('Работает магический метод setitem')
        return super().__setitem__(item, value)

    def __str__(self):
        print('Работает магический метод str')
        return super().__str__()

    def __len__(self):
        print('Работает магический метод len')
        return super().__len__()


lst = MyList(['Jone', 'Snow', 'Java'])  # __new__ и __init__

if not lst[2] == 'Python':      # __getitem__
    lst[2] = 'Python'           # __setitem__

print(lst)          #  __str__
print(len(lst))     #  __len__

