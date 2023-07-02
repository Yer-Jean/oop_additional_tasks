"""Эта задача взята из урока 13.2 пункт 9
Задача со звездочкой №1:

Создайте класс DataBase:
Реализуйте магический метод __new__ класса DataBase таким образом,
что экземпляр этого класса должен присутствовать гарантированно в одном
экземпляре при работе программы. То есть одновременно два объекта класса DataBase
быть не должно. При попытке создать второй экземпляр просто возвращаем ссылку на
ранее созданный экземпляр.
Ожидаемый вывод:
db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(db is db2)
True

Решение взято из примера паттерна Singleton (тип класса, который может быть только в одном экземпляре:
https://proproprogs.ru/python_oop/magicheskiy-metod-new-primer-patterna-singleton
https://ru.stackoverflow.com/questions/1025187/Зачем-нужен-new-и-каково-его-практическое-применение
https://docs-python.ru/tutorial/klassy-jazyke-python/ispolzovanie-new-klassah/
"""

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(db is db2)  # True
print(db2.connect())  # соединение с БД: root2, 5678, 40
""" Почему так произошло? Якобы создался второй экземпляр... Все просто. Мы здесь действительно видим первый объект.
Но при повторном вызове DataBase() также был вызван магический метод __init__ с новым набором аргументов и локальные
свойства изменили свое значение.
Мы можем здесь поставить «костыль» специально для метода __init__, чтобы не выполнять его если объект уже создан. 
Но правильнее было бы здесь переопределить еще один магический метод __call__
Источник: https://proproprogs.ru/python_oop/magicheskiy-metod-new-primer-patterna-singleton"""