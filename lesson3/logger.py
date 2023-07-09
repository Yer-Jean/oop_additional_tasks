"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""


class Logger:

    def __init__(self, filename):
        self.filename = filename
    
    def __call__(self, log_string, *args, **kwargs):
        with open(self.filename, 'w') as f:
            f.write(log_string)


logger = Logger("log.txt")
logger("This is a test message.")
