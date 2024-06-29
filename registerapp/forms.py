
from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(forms.ModelForm):   
    class Meta:
        model=User
        fields=['email','contact_number','address','username','code']
        labels={'email':'Email'}

class LoginForm(forms.Form):
    class Meta:
        model=User
        fields=['username','code']




        
