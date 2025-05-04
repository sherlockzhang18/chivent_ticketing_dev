from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name")

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
