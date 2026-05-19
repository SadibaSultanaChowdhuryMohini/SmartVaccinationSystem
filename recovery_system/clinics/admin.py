from django.contrib import admin
from .models import Clinic, Appointment

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):

    list_display = ('name', 'location', 'contact_number', 'opening_hours', 'vaccine_price_range','email')
    search_fields = ('name', 'location')
    list_filter = ('location',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ('user_name', 'clinic', 'date', 'time_slot', 'status')
    search_fields = ('user_name', 'clinic__name')
    list_filter = ('status', 'date')
