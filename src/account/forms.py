from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import MyUser


class MyCreationForm(UserCreationForm):
    username = forms.CharField(label='Имя')
    email = forms.EmailField(label='email')

    class Meta:
        model = MyUser
        fields = ('username', 'email')
        