from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())