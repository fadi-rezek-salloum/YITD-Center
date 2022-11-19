import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'country', 'phone', 'address',)


class UserChangeForm(UserChangeForm):
    password = None
    email = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'country', 'phone', 'address',)
