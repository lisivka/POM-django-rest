from django import forms
from django.forms import TextInput, Textarea, NumberInput

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = ['name', 'description', 'count', 'year', 'date_of_issue']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Input name"
            }),

            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Input description"
            }),

            "count": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Input count"
            }),
            "date_of_issue": NumberInput(attrs={
                'type': 'date',
                'placeholder': "date_of_issue"
            }),
        }
