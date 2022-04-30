from django import forms

from .models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'phone',
            'avatar',
        ]
    
    # Для сравнения двух паролей после ввода пароля