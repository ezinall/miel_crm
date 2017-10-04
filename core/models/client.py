# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


LEN_FIELD = 100


class Client(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Имя')
    surname = models.CharField(max_length=LEN_FIELD, blank=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=LEN_FIELD, blank=True, verbose_name='Отчество')
    email = models.EmailField(blank=True, verbose_name='Почта')
    phone = models.CharField(max_length=LEN_FIELD, blank=True, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.surname + ' ' + self.name
