from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'})
    )

    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'})
    )

    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'})
    )

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'})
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Input password'})
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
