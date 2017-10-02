# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from .property import FlatType

LEN_FIELD = 100
DEF_INTEGER = 0


class NumberRooms(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Количество комнат')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Количество комнат'
        verbose_name_plural = 'Количество комнат'

    def __str__(self):
        return self.name


class RepairType(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Ремонт')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Ремонт'
        verbose_name_plural = 'Ремонт'

    def __str__(self):
        return self.name


class NamePlace(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='ЖК')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'ЖК'
        verbose_name_plural = 'ЖК'

    def __str__(self):
        return self.name


class HouseType(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Тип дома')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Тип дома'
        verbose_name_plural = 'Типы домов'

    def __str__(self):
        return self.name


class ParkingType(models.Model):  # наземная многоуровневая подземная на крыше
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Парковка')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Парковка'
        verbose_name_plural = 'Парковка'

    def __str__(self):
        return self.name


class PriseType(models.Model):  # ₽ $ €
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Валюта')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'

    def __str__(self):
        return self.name


class SaleType(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Тип продажи')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Тип продажи'
        verbose_name_plural = 'Типы продажи'

    def __str__(self):
        return self.name


class CommType(models.Model):  # ₽ $ €
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Валюта')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'

    def __str__(self):
        return self.name


class FlatStatus(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Статус')
    color = models.CharField(max_length=LEN_FIELD, verbose_name='Цвет')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Metro(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Название')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Метро'
        verbose_name_plural = 'Метро'

    def __str__(self):
        return self.name


class Flat(models.Model):
    owner = models.ForeignKey('core.Client', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Собственник')
    date_start = models.DateField(blank=True, null=True, verbose_name='Начало продаж')

    app_type = models.ForeignKey(FlatType, default=0, verbose_name='Тип недвижимости')

    cadastral = models.CharField(max_length=LEN_FIELD, blank=True, verbose_name='Кадастровый номер')
    rooms = models.ForeignKey(NumberRooms, default=0, verbose_name='Количество комнат')
    apartments = models.BooleanField(default=False, verbose_name='Апартаменты')
    penthouse = models.BooleanField(default=False, verbose_name='Пентхаус')
    total_area = models.FloatField(verbose_name='Общая площадь')
    floors = models.IntegerField(verbose_name='Этажей в доме')
    floor = models.IntegerField(verbose_name='Этаж')  # validators=[1, floors],
    rooms_area = models.CharField(max_length=LEN_FIELD, verbose_name='Площадь комнат')
    living_area = models.FloatField(verbose_name='Жилая площадь')
    kitchen_area = models.FloatField(verbose_name='Кухня')
    loggia = models.IntegerField(default=0, verbose_name='Лоджия')  # validators=[0, 4],
    balcony = models.IntegerField(default=0, verbose_name='Балкон')  # validators=[0, 4],
    windows_yard = models.BooleanField(blank=True, verbose_name='Во двор')
    windows_street = models.BooleanField(blank=True, verbose_name='На улицу')
    separate_bath = models.IntegerField(default=0, verbose_name='Раздельные санузлы')  # validators=[0, 4],
    combine_bath = models.IntegerField(default=0, verbose_name='Совмещенные санузлы')  # validators=[0, 4],
    repairs = models.ForeignKey(RepairType, default=0, verbose_name='Ремонт')
    phone = models.BooleanField(default=True, verbose_name='Телефон')

    metro = models.ForeignKey(Metro, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Метро')

    name_place = models.ForeignKey(NamePlace, blank=True, null=True, verbose_name='Название ЖК')
    year = models.PositiveIntegerField(blank=True, verbose_name='Год постройки')  # validators=[1420, int(date.today().year)],
    house_type = models.ForeignKey(HouseType, default=3, verbose_name='Тип дома')
    house_ver = models.CharField(max_length=LEN_FIELD, blank=True, verbose_name='Серия дома')
    ceiling = models.FloatField(default=2.7, verbose_name='Высота потолков')  # validators=[1, 10],
    pas_lift = models.IntegerField(default=DEF_INTEGER, verbose_name='Пассажирский лифт')  # validators=[0, 4],
    ser_lift = models.IntegerField(default=DEF_INTEGER, verbose_name='Грузовой лифт')  # validators=[MinValueValidator(0), MaxValueValidator(4)],
    ramp = models.BooleanField(default=True, verbose_name='Пандус')
    chute = models.BooleanField(default=True, verbose_name='Мусоропровод')
    parking = models.ForeignKey(ParkingType, default=0, verbose_name='Парковка')

    video = models.URLField(blank=True, verbose_name='Видео')
    info = models.TextField(verbose_name='Описание')

    prise = models.PositiveIntegerField(default=DEF_INTEGER, verbose_name='Цена')
    prise_type = models.ForeignKey(PriseType, default=0, verbose_name='Валюта')
    mortgage = models.BooleanField(default=True, verbose_name='Возможна ипотека')
    sale_type = models.ForeignKey(SaleType, default=0, verbose_name='Тип продажи')
    bonus = models.BooleanField(default=False, verbose_name='Бонус агенту')

    major = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Ответственный')
    comm = models.CharField(max_length=LEN_FIELD, verbose_name='Комиссия')
    comm_type = models.ForeignKey(CommType, default=0, verbose_name='Валюта')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Название')
    active = models.BooleanField(default=True, verbose_name='Активный')
    calls = models.IntegerField(default=0, verbose_name='Звонки')
    views = models.IntegerField(default=0, verbose_name='Показы')
    status = models.ForeignKey(FlatStatus, default=1, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Статус')

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.name
