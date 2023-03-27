from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ServicesADomicile.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username': 'Username'}
        required = True

