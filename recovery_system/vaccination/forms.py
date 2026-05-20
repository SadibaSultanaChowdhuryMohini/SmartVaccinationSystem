
from django import forms
from .models import Child
from clinics.models import Clinic

class ChildRegistrationForm(forms.ModelForm):

    assigned_clinic = forms.ModelChoiceField(
        queryset=Clinic.objects.all(),
        empty_label="Select an Assigned Clinic",
        widget=forms.Select(attrs={'class': 'form-select', 'style': 'border-radius: 10px;'})
    )

    class Meta:
        model = Child
        fields = ['child_name', 'dob', 'gender', 'weight', 'assigned_clinic']
        widgets = {
            'child_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter child full name', 'style': 'border-radius: 10px;'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'border-radius: 10px;'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'style': 'border-radius: 10px;'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight in kg', 'step': '0.1', 'style': 'border-radius: 10px;'}),
        }