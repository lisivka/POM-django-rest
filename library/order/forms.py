from django import forms
from .models import Order
from book.models import Book
from authentication.models import CustomUser


class CustomUserField(forms.ModelChoiceField):
    def label_from_instance(self, member):
        return f"{member.first_name} {member.last_name} ({member.email} )"


class CustomBookField(forms.ModelChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name


class OrderForm(forms.ModelForm):
    user = CustomUserField(queryset=CustomUser.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control select-input'})

    )
    book = CustomBookField(queryset=Book.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control select-input'})

    )

    class Meta:
        model = Order
        fields = ("user", "book", "plated_end_at", "end_at", )

        widgets = {
            'end_at': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'plated_end_at': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }
        labels = {
            'user': "user",
            'book': "book",
            'end_at': "Returned at",
            'plated_end_at': "Must returned at"
        }