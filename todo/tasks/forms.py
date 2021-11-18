from django import forms

from django.forms import ModelForm

from .models import *


class TaskForm(ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter task'}))
    class Meta:
        model = Task
        fields = '__all__' #['title', 'description', 'status', 'priority', 'due_date']