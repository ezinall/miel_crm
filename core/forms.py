from django import forms

# Create your forms here.

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['director', 'create_date']
