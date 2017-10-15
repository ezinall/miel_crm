# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from app_flat.models import FlatUsage

LEN_FIELD = 100


class TaskPriority(models.Model):
    name = models.CharField(max_length=LEN_FIELD, verbose_name='Приоритете')

    class Meta:
        verbose_name = 'Приоритете'
        verbose_name_plural = 'Приоритеты'

    def __str__(self):
        return self.name


class Task(models.Model):
    director = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Постановщик')
    target = models.ForeignKey(FlatUsage, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Объект')
    priority = models.ForeignKey(TaskPriority, default=2, verbose_name='Приоритет')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    deadline = models.DateField(blank=True, null=True, verbose_name='Срок')
    label = models.CharField(max_length=LEN_FIELD, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Текст')
    active = models.BooleanField(default=True, verbose_name='Активный')

    def get_short_label(self):
        if len(self.label) >= 40:
            return self.label[:40] + ' ...'
        else:
            return self.label

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
        return self.task.label


class TaskExecutor(models.Model):
    task = models.ForeignKey(Task, verbose_name='Задач')
    executor = models.ForeignKey(User, default=1, verbose_name='Исполнтель')
    done = models.BooleanField(default=False, verbose_name='Выполнено')

    class Meta:
        verbose_name = 'Задача-Исполинтель'
        verbose_name_plural = 'Задача-Исполинтели'

    def __str__(self):
        return self.task.label
