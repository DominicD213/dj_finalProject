# admin.py
from django.contrib import admin
from .models import Location
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class LocationAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view
    list_display = ('name', 'country', 'latitude', 'longitude')
    
    # Add search functionality for specific fields
    search_fields = ['name', 'country']
    
    # Add filter options for easier navigation
    list_filter = ('country',)

# Register the model with its custom admin class
admin.site.register(Location, LocationAdmin)

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

