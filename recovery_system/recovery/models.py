from datetime import timedelta
from django.db import models
from vaccination.models import VaccinationSchedule

class RecoveryPlan(models.Model):
    REASON_CHOICES = (
        ('Forgot', 'Forgot'),
        ('Sick', 'Sick'),
        ('Travel', 'Travel'),
        ('No Slot', 'No Slot'),
    )
    vaccination_record = models.ForeignKey(VaccinationSchedule,on_delete=models.CASCADE,related_name='recovery_plans')
    reason = models.CharField(max_length=50,choices=REASON_CHOICES)
    suggested_date = models.DateField()
    image = models.ImageField(upload_to='profile/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (
            self.vaccination_record.child.full_name
        )
    def generate_plan(self):
        child = (self.vaccination_record.child.full_name)
        return f"Recovery plan for {child}"
    def get_instruction(self):
        vaccine = (self.vaccination_record.vaccine.name)
        return (f"Take {vaccine} vaccine "f"on {self.suggested_date}")

class ForgotRecoveryPlan(RecoveryPlan):
    reminder_frequency = models.CharField(max_length=100)
    def generate_plan(self):
        return (f"Reminder every "f"{self.reminder_frequency}")
    def get_instruction(self):
        return ("Please visit clinic as soon as possible.")

class SickRecovery(RecoveryPlan):
    delay_days = models.IntegerField()
    def generate_plan(self):
        new_date = (self.suggested_date +timedelta(days=self.delay_days))
        child = (self.vaccination_record.child.full_name)
        return (f"Recovery plan for "f"{child} on {new_date}")
    def get_instruction(self):
        return "Take vaccine after recovery."

class TravelRecovery(RecoveryPlan):
    clinic_name = models.CharField(max_length=100)
    def generate_plan(self):
        return (f"Visit nearest clinic: "f"{self.clinic_name}")
    def get_instruction(self):
        return ("Take vaccine from nearest clinic.")

class NoSlotRecovery(RecoveryPlan):
    alternative_clinic = models.CharField(max_length=100)
    def generate_plan(self):
        return (f"Alternative clinic: "f"{self.alternative_clinic}")
    def get_instruction(self):
        return ("Visit alternative clinic ""for vaccination.")