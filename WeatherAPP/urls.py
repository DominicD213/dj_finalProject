# WeatherAPP/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.weather_dashboard, name='dashboard'),  # URL pattern for dashboard
    path('location/<int:location_id>/', views.location_weather, name='location_weather'),
    path('add-location/', views.add_location, name='add_location'),
    path('', views.weather_dashboard, name='weather_dashboard'),
]
