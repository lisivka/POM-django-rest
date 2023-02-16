from django import forms
from django.core.exceptions import ValidationError
from authentication.models import CustomUser


class UpdateUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'role'
        )

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 1:
            raise ValidationError('Enter name')
        if first_name == 'admin':
            raise ValidationError(f'{first_name} reserved name')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 1:
            raise ValidationError('Enter lastname')
        if last_name == "admin":
            raise ValidationError(f'{last_name} reserved name')

        return last_name

    def clean_middle_name(self):
        middle_name = self.cleaned_data['middle_name']
        if len(middle_name) < 1:
            raise ValidationError('Enter middle name')
        if middle_name == 'admin':
            raise ValidationError(f'{middle_name }reserved name')

        return middle_name


class CreateUser(UpdateUser):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')

        return cd['password2']


class LoginUser(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ResetPassword(forms.Form):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def clean_new_password2(self):
        cd = self.cleaned_data
        if cd['new_password'] != cd['new_password2']:
            raise forms.ValidationError('Passwords don\'t match.')

        return cd['new_password2']