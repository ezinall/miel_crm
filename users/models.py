# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

LEN_FIELD = 100


class UserType(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Должность')
    alias = models.SlugField(max_length=LEN_FIELD)


class User(models.Model):
    position = models.ForeignKey(UserType, verbose_name='Должность')
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Имя')
    surname = models.CharField(max_length=LEN_FIELD, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=LEN_FIELD, verbose_name='Отчество')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=LEN_FIELD, verbose_name='Телефон')
