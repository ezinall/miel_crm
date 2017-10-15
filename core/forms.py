# -*- coding: utf-8 -*-
from django import forms

# Create your forms here.

from .models import TaskExecutor, Task, TaskComments


class TaskExecutorForm(forms.ModelForm):
    class Meta:
        model = TaskExecutor
        exclude = ['task', 'done']

    def __init__(self, *args, **kwargs):
        super(TaskExecutorForm, self).__init__(*args, **kwargs)
        self.fields['executor'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['executor'].widget.attrs.update({'class': 'form-control form-control-sm optional', 'size': '5'})


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['director', 'create_date', 'active']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['target'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['deadline'].widget.attrs.update({'class': 'form-control form-control-sm', 'type': 'datetime-local', 'placeholder': 'дд.мм.гггг'})
        self.fields['label'].widget.attrs.update({'class': 'form-control form-control-sm', 'placeholder': 'Заголовок задачи'})
        self.fields['text'].widget.attrs.update({'class': 'form-control form-control-sm', 'rows': '5', 'placeholder': 'Содержание'})


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskComments
        exclude = ['task', 'author', 'date_pub']

    def __init__(self, *args, **kwargs):
        super(TaskCommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control form-control-sm', 'rows': '5', 'placeholder': 'Текст'})
