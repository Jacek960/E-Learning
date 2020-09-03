from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=75, required=True, help_text="Wymagane pole - wprowadz poprawny email adres")
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email','password1', 'password2')