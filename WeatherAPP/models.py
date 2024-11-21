from django.db import models
from users.models import User
from django.contrib.auth.admin import UserAdmin

class Location(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default='Unknown')  # Default value
    latitude = models.FloatField(default=0.0)  # Default value
    longitude = models.FloatField(default=0.0)  # Default value

    def __str__(self):
        return f"{self.name}, {self.country}"

# The rest of your models can remain as is
class WeatherData(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='weather_data')
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    weather_description = models.TextField()
    forecast_date = models.DateField()

    def __str__(self):
        return f"Weather on {self.forecast_date} for {self.location}"

class Alert(models.Model):
    CONDITION_CHOICES = [
        ('temperature', 'Temperature'),
        ('rain', 'Rain'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='alerts')
    condition_type = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    threshold = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.condition_type} alert for {self.location} by {self.user}"

class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    
    # Fields to include in the search bar
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Fields to filter users in the admin panel
    list_filter = ('is_active', 'is_staff')
    
    # Specify fields for adding/editing users
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Fields that should be editable in the form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')}
        ),
    )
    
    # This makes it possible to delete users from the admin
    actions = ['delete_selected']
