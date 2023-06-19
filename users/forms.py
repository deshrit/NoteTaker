import re
from typing import Any, Dict
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm, 
    PasswordResetForm,
    SetPasswordForm
)


class SignupForm(UserCreationForm):
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control border border-dark',
                'placeholder': 'Email ...'
            }
        ),
        error_messages={"invalid": "Invalid email address"}
    )

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border border-dark',
                'placeholder': 'Username ...'
            }
        ),
        help_text="Only letters, number, _ and . allowed"
    )
    password1 = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control border border-dark',
                'placeholder': 'Password ...'
            }
        ),
        help_text="At least 8 characters"
    )
    password2 = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control border border-dark',
                'placeholder': 'Re-type Password ...'
            }
        )
    )

    def clean_username(self):
        cleaned_username = self.cleaned_data.get('username')
        username_pattern = r"^([a-zA-Z_\.]){1}([a-zA-Z_\.0-9])+$"
        if not re.search(username_pattern, cleaned_username):
            raise forms.ValidationError("Invalid username")
        if User.objects.filter(username=self.cleaned_data.get('username')):
            raise forms.ValidationError("Username already exists.")
        return cleaned_username
    
    def clean_email(self):
        cleaned_email = self.cleaned_data.get('email')
        if User.objects.filter(email=cleaned_email):
            raise forms.ValidationError("Email already exists.")
        return cleaned_email

    # order of the fields
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    

class LoginForm(AuthenticationForm):

    error_messages = {
        "invalid_login": "Invalid Username or Password.",
        "inactive": "This account is inactive.",
    }
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "class": "form-control border border-dark",
            "placeholder": "Username ..."
        })
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control border border-dark",
                "placeholder": "Password ..."
            }
        )
    )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': 'Only letters, number, _ and . allowed'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',

                },
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image': ''
        }


class PassResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control border border-dark',
                'placeholder': 'Email ...'
            }
        ),
        error_messages={"invalid": "Invalid email address"}
    )

class PassNewForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control border border-dark",
                "placeholder": "New Password ..."
            }),
        strip=False,
        help_text="Only letters, number, _ and . allowed"
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control border border-dark",
                "placeholder": "Re-type New Password ..."
            }),
    )