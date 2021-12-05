from django import forms
from django.forms import ModelForm
from .models import *

class TodoForm(ModelForm):
    class Meta:
        model = todo_list
        fields = '__all__'