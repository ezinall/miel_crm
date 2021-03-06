# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

LEN_FIELD = 100


class TransactionType(models.Model):  # аренда, продажа
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Тип сделки')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Тип сделки'
        verbose_name_plural = 'Типы сделок'

    def __str__(self):
        return self.name


class PropertyType(models.Model):  # тип недвижимости жилая коммерческая
    transaction = models.ForeignKey(TransactionType, verbose_name='Тип сделки')
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Тип недвижимости')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Тип недвижимости'

    def __str__(self):
        return self.name


class FlatType(models.Model):  # Квартира, Квартира в новостройке, Комната, Доля в квартире, Дом/Дача, Коттедж,
    # Таунхаус, Часть дома, Участок
    property = models.ForeignKey(PropertyType, verbose_name='Тип недвижимости')
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Тип объекта')
    alias = models.SlugField(max_length=LEN_FIELD)

    class Meta:
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Типы объектов'

    def __str__(self):
        return self.name
