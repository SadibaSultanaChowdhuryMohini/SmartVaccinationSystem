from django import forms
from .models import RecoveryPlan

class RecoveryForm(forms.ModelForm):
    class Meta:
        model = RecoveryPlan
        fields = [
            'vaccination_record',
            'reason',
            'suggested_date',
            'image',
        ]