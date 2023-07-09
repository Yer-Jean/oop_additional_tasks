"""Задача 3. Контекстный менеджер
Создайте свой контекстный менеджер для работы с файлами на основе встроенного менеджера open.
Пусть при открытии файла в консоль выводится сообщение об открытии файла, а при закрытии — сообщение
о закрытии с информацией о времени, на которое файл был открыт.
Ожидаемый вывод:

from time import perf_counter, sleep

class MyOpen:
    pass

with MyOpen('countries.txt', 'r') as fp:
    content = fp.read()
    print('Чтение данных 2 секунды...')
    sleep(2)

print('Продолжение кода...')

Вывод в консоли:
Файл успешно открыт
Чтение данных 2 секунды...
Файл был открыт 2.000626699998975 секунд и теперь успешно закрыт.
Продолжение кода...

"""

from time import perf_counter, sleep

class MyOpen:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.counter = perf_counter()
        self.fp = open(self.filename, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()
        total_counter = perf_counter() - self.counter
        print(f'Файл был открыт {total_counter} секунд и теперь успешно закрыт.')

with MyOpen('log.txt', 'r') as fp:
    content = fp.read()
    print('Чтение данных 2 секунды...')
    sleep(2)

print('Продолжение кода...')