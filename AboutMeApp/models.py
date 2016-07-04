from django.db import models


class Work(models.Model):
    name = models.CharField(verbose_name='Организация', max_length=32)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16)
    desc = models.TextField(verbose_name='Описание деятельности компании')
    date_start = models.DateField(verbose_name='Дата начала')
    date_finish = models.DateField(verbose_name='Дата завершения', blank=True, null=True)
    logo = models.CharField(verbose_name='Логотп компании', max_length=64, blank=True)


class Study(models.Model):
    name = models.TextField(verbose_name='Учебное заведение')
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    faculty = models.TextField(verbose_name='Факультет')
    specialty = models.TextField(verbose_name='Специальность')
    degree = models.CharField(verbose_name='Уровень образования', max_length=128)
    date_start = models.DateField(verbose_name='Дата начала обучения')
    date_finish = models.DateField(verbose_name='Дата завершения обучения', blank=True, null=True)
    logo = models.CharField(verbose_name='Логотп', max_length=64, blank=True)


class Hobby(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32)
    ico_fa = models.CharField(verbose_name='Иконка (FA)', max_length=64, blank=True)


class UserInfo(models.Model):
    date_birthday = models.DateField(verbose_name='Дата рождения')
    first_name = models.CharField(verbose_name='Имя', max_length=32)
    last_name = models.CharField(verbose_name='Фамилия', max_length=32)
    second_name = models.CharField(verbose_name='Отчество', max_length=32)
    place_birthday = models.CharField(verbose_name='Место рождения', max_length=64)
    hobbies = models.ManyToManyField(Hobby)