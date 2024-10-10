
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CadastroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        widgets = {
            'email':forms.EmailInput,
            'password':forms.PasswordInput,
        }
