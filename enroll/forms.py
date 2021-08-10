from django import forms
from .models import *

# print('-------------------\n', DemoUser, '\n--------------------')


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = DemoUser
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'id': 'passwordid'})
        }
