"""Задача 1. Обратный итератор Создайте класс-итератор ReIterator, который возвращает в обратном порядке элементы списка.
Ожидаемый вывод:
x = ReIterator([1, 2, 3, 4])
for i in x:
    print(i)
4
3
2
1


Задача 2. Длина итератора
Допишите класс ReIterator, чтобы с его экземпляром работала встроенная функция
len и выполнялось такое поведение:
x = ReIterator([1, 2, 3, 4])
print(len(x))
4
"""

class ReIterator:
    def __init__(self, data_list):
        self.data_list = data_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.data_list:
            return self.data_list.pop(-1)
        raise StopIteration

    def __len__(self):
        return len(self.data_list)


x = ReIterator([1, 2, 3, 4])
print(len(x))

for i in x:
    print(i)

print(len(x))