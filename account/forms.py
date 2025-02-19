# forms.py
from django import forms
from django.contrib.auth import authenticate
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'required': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'required': True,
        })
    )
    # remember_me = forms.BooleanField(
    #     required=False,
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'form-check-input',
    #     })
    # )
    
class ExcelUploadForm(forms.Form):
    file = forms.FileField()



class MatchForm(forms.Form):
    register_no = forms.CharField(max_length=15)
    dob = forms.DateField()
    captcha = CaptchaField()  # This adds the CAPTCHA field to the form
