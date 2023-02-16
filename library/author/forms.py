from django import forms
from django.core.exceptions import ValidationError
from author.models import Author


class CreateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name': 'Author name',
        }
    