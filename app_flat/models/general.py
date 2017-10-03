# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from .flat_usage import FlatUsage

import uuid

LEN_FIELD = 100


def image_path_with_name(instance, filename):
    return 'apa_objects/%s/image/%s.%s' % (instance.id, str(uuid.uuid4()).split('-')[-1], filename.split('.')[-1])


class FlatImage(models.Model):
    apartment = models.ForeignKey(FlatUsage, on_delete=models.CASCADE, verbose_name='Квартира')
    image = models.ImageField(upload_to=image_path_with_name, blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.apartment.name or None


class FlatComment(models.Model):
    apartment = models.ForeignKey(FlatUsage, on_delete=models.CASCADE, verbose_name='Квартира')
    author = models.ForeignKey(User, verbose_name='Автор')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.apartment.name or None
