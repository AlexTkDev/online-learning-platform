from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .enums import Role

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    role = forms.ChoiceField(choices=[(role.name, role.value) for role in Role],
                             widget=forms.Select(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "*******************"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "*******************"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Name"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "*******************"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
