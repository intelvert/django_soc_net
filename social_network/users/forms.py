from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
#from django.utils.translation import gettext_lazy as _
from .validators import username_validator


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, 
                               required=True, 
                               validators=[username_validator],
                               help_text="30 characters or fewer. Letters, digits, \"_\" and \"-\" only.")
    
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
