from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    first_name= forms.CharField(max_length=200)
    last_name= forms.CharField(max_length=200)
    email =forms.EmailField()
    class Meta:
        model = User 
        fields=['first_name','last_name','username','email','password1','password2']