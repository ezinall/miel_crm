# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

from django.contrib.auth.models import User, Group

LEN_FIELD = 100


class UserPositionType(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=11, blank=True, verbose_name='Номер телефона')
    patronymic = models.CharField(max_length=30, blank=True, verbose_name='Отчество')
    position = models.ForeignKey(UserPositionType, default=1, verbose_name='Должность')


class GroupHead(models.Model):
    group = models.OneToOneField(Group)
    leader = models.OneToOneField(User, verbose_name='Руководитель')


