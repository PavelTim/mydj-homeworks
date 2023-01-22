from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    group = models.CharField(max_length=10, verbose_name='Класс')

    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, related_name='students')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name

# class Lesson(models.Model):
#     students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='lessons')
#     teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
#
#     class Meta:
#         verbose_name = 'Урок'
#         verbose_name_plural = 'Уроки'
