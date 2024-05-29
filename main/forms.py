from django import forms
from .models import ToDoNote


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoNote
        fields = ['content']