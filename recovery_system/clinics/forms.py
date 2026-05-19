from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user_name', 'clinic', 'date', 'time_slot', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }