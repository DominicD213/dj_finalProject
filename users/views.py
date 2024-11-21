
from django.shortcuts import render, redirect
import logging
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm  # Import your custom form

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request, user)
            logger.info("User logged in: %s", user.username)
            return redirect('weather_dashboard')  # Redirect to a success page
        else:
            logger.error("Invalid login attempt: %s", form.errors)
            return render(request, 'users/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})