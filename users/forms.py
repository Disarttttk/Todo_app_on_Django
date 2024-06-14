from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm

from .models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    error_messages = {
        'invalid_login': (
            "Неверное имя пользователя или пароль. Попробуйте ещё раз."
        )
    }

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class UserProfileForm(UserChangeForm):
    images = forms.ImageField(required=False)
    username = forms.CharField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = (
            'images',
            'username',
            'email'
        )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField()
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()