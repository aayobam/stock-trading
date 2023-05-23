from django.contrib.auth import get_user_model
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
