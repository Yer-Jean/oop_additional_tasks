"""Задача 1
Создайте класс TodoList, который хранит ваши задачи. Реализуйте магические методы, которые позволят добиться следующего поведения:
# >>> tasks = ['task1', 'task2']
# >>> list1 = TodoList(tasks)
# >>> print(repr(list1))
# TodoList(list[str])
# >>> print(list1)
# task1
# task2

Задача 2
Продолжение задачи 1
Реализуйте магический метод, который позволит складывать два списка задач (экземпляра класса
TodoList) и получать новый список, содержащий задачи обоих сладываемых списков:
# >>> list2 = TodoList(['task3', 'task4'])
# >>> list3 = list1 + list2
# >>> print(list3)
# task1
# task2
# task3
# task4

Задача 3
Продолжение задачи 2
Дополните класс TodoList, чтобы выполнялось следующее поведение:
# >>> print(len(list3))
# 4
"""

class TodoList:

    def __init__(self, tasks: list):
        self.tasks = tasks

    def __repr__(self):
        return f"{self.__class__.__name__} {self.tasks}"

    def __str__(self):
        return '\n'.join(task for task in self.tasks)

    def __add__(self, other):
        return TodoList(self.tasks + other.tasks)

    def __len__(self):
        return len(self.tasks)

tasks1 = ['task1', 'task2']
tasks2 = ['task3', 'task4']
list1 = TodoList(tasks1)
list2 = TodoList(tasks2)
list3 = list1 + list2

print(repr(list3))
print(list3)

print(len(list3))
