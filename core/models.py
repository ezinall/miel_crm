# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10, blank=True, verbose_name='Номер телефона')
    patronymic = models.CharField(max_length=30, blank=True, verbose_name='Отчество')
