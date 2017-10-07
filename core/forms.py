# -*- coding: utf-8 -*-
from django import forms

# Create your forms here.

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['director', 'create_date', 'done', 'active']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['executor'].widget.attrs.update({'class': 'form-control form-control-sm optional', 'size': '5'})
        self.fields['target'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['deadline'].widget.attrs.update({'class': 'form-control form-control-sm', 'type': 'datetime-local', 'placeholder': 'дд.мм.гггг'})
        self.fields['label'].widget.attrs.update({'class': 'form-control form-control-sm', 'placeholder': 'Заголовок задачи'})
        self.fields['text'].widget.attrs.update({'class': 'form-control form-control-sm', 'rows': '5', 'placeholder': 'Содержание'})
