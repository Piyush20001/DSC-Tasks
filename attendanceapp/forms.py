from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class attendeeregistration(forms.Form):
    fullname=forms.CharField(required=True,label= 'Fullname',max_length=50)
    username=forms.CharField(required=True,label= 'Username',max_length=30)
    email=forms.CharField(required=True,label= 'Email',max_length=30)
    batch=forms.CharField(required=True,label= 'Batch',max_length=30)
    enrollno=forms.CharField(required=True,label= 'Enrollment No.',max_length=15)
    branch=forms.CharField(required=True,label= 'Branch',max_length=10)
    password=forms.CharField(required=True,label= 'Password',max_length=30,widget = forms.PasswordInput())
    