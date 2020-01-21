from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer
from django import forms
import datetime


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['dob', 
                  'first_name',
                  'last_name',
                  'gender',
                  'nationality', 
                  'hobby', 
                  'favorite_book', 
                  'picture']
