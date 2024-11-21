from django.shortcuts import render, redirect
from .models import WeatherData, Location
from .task import update_weather_data
from .forms import LocationForm
from django.db.models import Q  # For searching by name

def weather_dashboard(request):
    # Get all locations
    locations = Location.objects.all()

    # Triggering the Celery task for each location
    for location in locations:
        update_weather_data.delay(location.id)  # This queues the task to be executed by Celery

    # If search query is present, filter the locations by name
    search_query = request.GET.get('search', '')
    if search_query:
        locations = locations.filter(name__icontains=search_query)

    return render(request, 'weather/dashboard.html', {
        'locations': locations,
        'search_query': search_query
    })

def location_weather(request, location_id):
    # Fetch the location and related weather data
    location = Location.objects.get(id=location_id)
    weather_data = WeatherData.objects.filter(location=location)
    return render(request, 'weather/location_weather.html', {'location': location, 'weather_data': weather_data})

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location_name = form.cleaned_data['name']
            # Check if location already exists
            location, created = Location.objects.get_or_create(name=location_name)
            if created:
                # Location created successfully, redirect to location's weather page
                return redirect('weather:location_weather', location_id=location.id)
            else:
                # Location already exists, display a message
                return render(request, 'weather/add_location.html', {'form': form, 'message': 'Location already exists.'})
    else:
        form = LocationForm()

    return render(request, 'weather/add_location.html', {'form': form})
