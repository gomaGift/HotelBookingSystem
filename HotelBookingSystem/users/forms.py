from django import forms
from django.contrib.auth.models import models
from .models import User
from django.contrib.auth.forms import UserCreationForm


class CustomLoginForm(forms.Form):
    phone_email = forms.CharField(max_length=100, label='Phone or Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-class'}))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'profile_pic', 'password1', 'password2']

    def save(self, commit=True):
            user = super().save(commit=False)
            user.username = f"{self.cleaned_data['first_name']}_{self.cleaned_data['last_name']}"
            if commit:
                user.save()
            return user   
