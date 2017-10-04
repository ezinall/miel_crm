# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

from django.contrib.auth.models import User, Group
from app_flat.models import FlatUsage

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


class Task(models.Model):
    director = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Постановщик')
    executor = models.ManyToManyField(User, related_name='task_executor', verbose_name='Исполнитель')
    target = models.ForeignKey(FlatUsage, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Объект')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    deadline = models.DateField(blank=True, null=True, verbose_name='Срок')
    label = models.CharField(max_length=LEN_FIELD, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Текст')
    done = models.BooleanField(default=False, verbose_name='Выполнено')
    active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.label


class TaskComments(models.Model):
    task = models.ForeignKey(Task, verbose_name='Объект')
    author = models.ForeignKey(User, verbose_name='Автор')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.task.name or None
