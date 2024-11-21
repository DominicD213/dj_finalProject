from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Assuming you have a custom User model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User  # Use your custom User model if you're not using Django's default User model
        fields = ('username', 'email', 'password1', 'password2')
