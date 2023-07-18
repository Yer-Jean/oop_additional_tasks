"""
Напишите класс Student, представляющий студента, имеющий следующие атрибуты:

- __slots__ = ('name', 'age', 'grades'): список атрибутов, доступных объекту.

Напишите класс Course, представляющий курс, имеющий следующие атрибуты:

- __slots__ = ('name', 'students'): список атрибутов, доступных объекту.
"""


class Student:
    __slots__ = ('name', 'age', 'grades')

    def __str__(self):
        return f'{self.name}'

class Course:
    __slots__ = ('name', 'students')

    def __str__(self):
        students_list = ' '.join(self.students[i].name for i in range(len(self.students)))
        return f'{self.name} - {students_list}'



student1 = Student()
student1.name = "John"
student1.age = 20
student1.grades = [90, 80, 85]

student2 = Student()
student2.name = "Jane"
student2.age = 21
student2.grades = [95, 85, 90]

course = Course()
course.name = "Math"
course.students = [student1, student2]
print(student1)
print(course)
