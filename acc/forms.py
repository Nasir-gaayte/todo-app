from pyexpat import model
from django import forms
from django import forms
from django.contrib.auth.models import User




class RegisterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password")