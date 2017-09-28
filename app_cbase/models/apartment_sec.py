# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

import uuid
from datetime import date

from core.models import User
from .owner import Owner
from .ad import ApartmentType

LEN_FIELD = 100
DEF_INTEGER = 0


def image_path_with_name(instance, filename):
    return 'apa_objects/%s/image/%s.%s' % (instance.id, str(uuid.uuid4()).split('-')[-1], filename.split('.')[-1])


class NumbersRooms(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Количество комнат')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Количество комнат'
        verbose_name_plural = 'Количество комнат'

    def __str__(self):
        return self.name


class RepairsType(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Ремонт')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Ремонт'
        verbose_name_plural = 'Ремонт'

    def __str__(self):
        return self.name


class NamesPlace(models.Model):
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


class Apartment(models.Model):
    owner = models.ForeignKey(Owner, blank=True, verbose_name='Собственник')
    date_start = models.DateTimeField(blank=True, verbose_name='Начало продаж')

    app_type = models.ForeignKey(ApartmentType, default=0, verbose_name='Тип недвижимости')

    cadastral = models.CharField(max_length=LEN_FIELD, blank=True, verbose_name='Кадастровый номер')
    rooms = models.ForeignKey(NumbersRooms, default=0, verbose_name='Количество комнат')
    apartments = models.BooleanField(default=False, verbose_name='Апартаменты')
    penthouse = models.BooleanField(default=False, verbose_name='Пентхаус')
    total_area = models.FloatField(verbose_name='Общая площадь')
    floors = models.IntegerField(default=1, verbose_name='Этажей в доме')
    floor = models.IntegerField(validators=[1, floors], verbose_name='Этаж')
    rooms_area = models.CharField(max_length=LEN_FIELD, verbose_name='Площадь комнат')
    living_area = models.FloatField(verbose_name='Жилая площадь')
    kitchen_area = models.FloatField(verbose_name='Кухня')
    loggia = models.IntegerField(default=0, validators=[0, 4], verbose_name='Лоджия')
    balcony = models.IntegerField(default=0, validators=[0, 4], verbose_name='Балкон')
    windows_yard = models.BooleanField(blank=True, verbose_name='Во двор')
    windows_street = models.BooleanField(blank=True, verbose_name='На улицу')
    separate_bath = models.IntegerField(default=0, validators=[0, 4], verbose_name='Раздельные санузлы')
    combine_bath = models.IntegerField(default=0, validators=[0, 4], verbose_name='Совмещенные санузлы')
    repairs = models.ForeignKey(RepairsType, default=0, verbose_name='Ремонт')
    phone = models.BooleanField(default=False, verbose_name='Телефон')

    name_place = models.ForeignKey(NamesPlace, blank=True, verbose_name='Название')
    year = models.PositiveIntegerField(validators=[1420, date.today().year], verbose_name='Год постройки')
    house_type = models.ForeignKey(HouseType, default=3, verbose_name='Тип дома')
    house_ver = models.CharField(max_length=LEN_FIELD, blank=True, verbose_name='Серия дома')
    ceiling = models.FloatField(default=2.7, validators=[1, 10], verbose_name='Высота потолков')
    pas_lift = models.IntegerField(validators=[0, 4], verbose_name='Пассажирский лифт')
    ser_lift = models.IntegerField(validators=[0, 4], verbose_name='Грузовой лифт')
    ramp = models.BooleanField(default=True, verbose_name='Пандус')
    chute = models.BooleanField(default=True, verbose_name='Мусоропровод')
    parking = models.ForeignKey(ParkingType, default=0, verbose_name='Парковка')

    image = models.ImageField(upload_to=image_path_with_name, blank=True, verbose_name='Фото')
    video = models.URLField(blank=True, verbose_name='Видео')
    info = models.TextField(verbose_name='Описание')

    prise = models.PositiveIntegerField(default=DEF_INTEGER, verbose_name='Цена')
    prise_type = models.ForeignKey(PriseType, default=0, verbose_name='Валюта')
    mortgage = models.BooleanField(default=True, verbose_name='Возможна ипотека')
    sale_type = models.ForeignKey(SaleType, default=0, verbose_name='Тип продажи')
    bonus = models.BooleanField(default=False, verbose_name='Бонус агенту')

    major = models.ForeignKey(User, blank=True, verbose_name='Ответственный')
    comm = models.CharField(max_length=LEN_FIELD, verbose_name='Комиссия')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Название')
    active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.name


class Comment(models.Model):
    apartment = models.ForeignKey(Apartment, verbose_name='Квартира')
    author = models.ForeignKey(User, verbose_name='Автор')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.apartment.name or None
