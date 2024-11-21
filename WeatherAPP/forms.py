from django import forms
from .models import Location

class LocationForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search for a location')