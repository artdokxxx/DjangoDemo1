from django.db import models


class Organization(models.Model):
    name = models.CharField(verbose_name='Организация', max_length=32, unique=True)
    site = models.URLField(verbose_name='Сайт', blank=True)
    place = models.CharField(verbose_name='Город', max_length=32)
    phone = models.CharField(verbose_name='Телефон', max_length=32, blank=True)
    logo = models.CharField(verbose_name='Логотип', max_length=64,
                            blank=True)
    desc = models.TextField(verbose_name='Описание деятельности компании', blank=True)


class EducationalOrganization(models.Model):
    name = models.CharField(verbose_name='Учебное заведение', max_length=32, unique=True)
    site = models.URLField(verbose_name='Сайт', blank=True)
    address = models.CharField(verbose_name='Город', max_length=32)
    phone = models.CharField(verbose_name='Телефон', max_length=32, blank=True)
    logo = models.CharField(verbose_name='Логотип', max_length=64,
                            blank=True)
    desc = models.TextField(verbose_name='Описание', blank=True)


class Work(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Организация')
    position = models.CharField(verbose_name='Должность', max_length=16)
    desc = models.TextField(verbose_name='Описание')
    date_start = models.DateField(verbose_name='Дата начала')
    date_finish = models.DateField(verbose_name='Дата завершения', blank=True, null=True)


class Study(models.Model):
    educational_organization = models.ForeignKey(EducationalOrganization, verbose_name='Учебное заведение')
    faculty = models.CharField(verbose_name='Факультет', max_length=256)
    specialty = models.CharField(verbose_name='Специальность', max_length=256)
    degree = models.CharField(verbose_name='Уровень образования', max_length=128)
    date_start = models.DateField(verbose_name='Дата начала обучения')
    date_finish = models.DateField(verbose_name='Дата завершения обучения', blank=True, null=True)


class Hobby(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32, unique=True)
    ico_fa = models.CharField(verbose_name='Иконка (FA)', max_length=64, blank=True)


class UserInfo(models.Model):
    date_birthday = models.DateField(verbose_name='Дата рождения')
    first_name = models.CharField(verbose_name='Имя', max_length=32)
    last_name = models.CharField(verbose_name='Фамилия', max_length=32)
    second_name = models.CharField(verbose_name='Отчество', max_length=32)
    place_birthday = models.CharField(verbose_name='Место рождения', max_length=64)
    hobbies = models.ManyToManyField(Hobby)