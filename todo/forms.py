from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, fields, widgets
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important', 'duedate']
        labels = {
            'title': "Task"
        }
        help_texts = {
            'title': "This is a helpful thing."
        }
        error_messages = {
            'title': {
                'max_length': _("The title is too long."),
            },
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Task'
                 }),
            'memo': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Details',
                'rows': 4
                 }),
            'important': forms.Select(attrs={
                'class': 'form-control form-control-lg',
                'default':'None'
                }),
            'duedate': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Due Date'
                }),
        }

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password"]
        labels = {

        }
        help_texts = {

        }
        error_messages = {

        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Username'
                 }),
            'password': forms.TextInput(attrs={ 
                'type': 'password',
                'class': 'form-control form-control-lg','placeholder': 'Password'
                 }),
        }