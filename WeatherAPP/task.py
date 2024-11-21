# WeatherAPP/tasks.py

from celery import shared_task
from .models import Location, WeatherData  # Import Location from models.py
import requests
from django.conf import settings

@shared_task
def update_weather_data(location_id):
    try:
        # Fetch the location object from models
        location = Location.objects.get(id=location_id)

        # Make an API call to fetch weather data (using the stored API key from settings)
        api_url = f"http://api.weatherapi.com/v1/current.json?key={settings.WEATHER_API_KEY}&q={location.name}"
        response = requests.get(api_url)
        
        # Check if the response is valid
        if response.status_code == 200:
            weather_data = response.json()
            
            # Extract weather data
            temperature = weather_data['current']['temp_c']
            humidity = weather_data['current']['humidity']
            wind_speed = weather_data['current']['wind_kph']
            weather_description = weather_data['current']['condition']['text']

            # Save the weather data in the WeatherData model
            WeatherData.objects.create(
                location=location,
                temperature=temperature,
                humidity=humidity,
                wind_speed=wind_speed,
                weather_description=weather_description,
                forecast_date=weather_data['location']['localtime'][:10],  # Extracting date only (YYYY-MM-DD)
            )

            return f"Weather updated for {location.name}"
        else:
            return f"Failed to fetch weather data for {location.name}. Status code: {response.status_code}"

    except Location.DoesNotExist:
        return f"Location with ID {location_id} not found."
    except Exception as e:
        return f"Error while updating weather data: {str(e)}"
