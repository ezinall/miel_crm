# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from app_flat.models import Flat

LEN_FIELD = 100


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10, blank=True, verbose_name='Номер телефона')
    patronymic = models.CharField(max_length=30, blank=True, verbose_name='Отчество')


class Task(models.Model):
    director = models.ForeignKey(User, verbose_name='Постановщик')
    executor = models.ManyToManyField(User, related_name='users_executor', verbose_name='Исполнитель')
    target = models.ForeignKey(Flat, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Объект')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    deadline = models.DateTimeField(blank=True, verbose_name='Срок')
    label = models.CharField(max_length=LEN_FIELD, blank=True, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.label


class CommentsTask(models.Model):
    task = models.ForeignKey(Task, verbose_name='Объект')
    author = models.ForeignKey(User, verbose_name='Автор')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.task.name or None


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
