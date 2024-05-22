from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.fields import forms

from .models import Message


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    pass


class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}), label=False)

    class Meta:
        model = Message
        fields = ["content"]
