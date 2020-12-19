from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, widgets
from .models import Todo

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
        }