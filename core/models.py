from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=10, verbose_name='Номер телефона')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
