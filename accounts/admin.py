from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'dob', 'phone_number', 'is_active', 'is_staff', 'is_superuser', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'date_joined']

admin.site.register(User, UserAdmin)

