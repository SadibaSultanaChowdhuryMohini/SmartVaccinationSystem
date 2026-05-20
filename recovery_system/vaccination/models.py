
from django.db import models
from django.conf import settings
from datetime import timedelta, date
from django.db.models.signals import post_save
from django.dispatch import receiver



class Vaccine(models.Model):
    name = models.CharField(max_length=200, unique=True)
    days_after_birth = models.IntegerField(help_text="Days after birth this should be taken")

    def __str__(self):
        return self.name



class Child(models.Model):
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    assigned_clinic = models.ForeignKey('clinics.Clinic', on_delete=models.SET_NULL, null=True, blank=True)

    child_name = models.CharField(max_length=200)
    dob = models.DateField()
    verified = models.BooleanField(default=False)
    gender = models.CharField(max_length=20, choices=(('male', 'Male'), ('female', 'Female')))
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def age(self):
        today = date.today()
        calculated_age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return calculated_age

    def __str__(self):
        return self.child_name



class VaccinationSchedule(models.Model):
    VERIFICATION_CHOICES = [('PENDING', 'Pending'), ('VERIFIED', 'Verified')]
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=200)
    scheduled_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    reminder_sent = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.child.child_name} - {self.vaccine_name}"


@receiver(post_save, sender=Child)
def create_child_vaccination_schedule(sender, instance, created, **kwargs):

    if created:
        all_vaccines = Vaccine.objects.all()
        for vaccine in all_vaccines:
            vaccine_date = instance.dob + timedelta(days=vaccine.days_after_birth)
            VaccinationSchedule.objects.create(
                child=instance,
                vaccine_name=vaccine.name,
                scheduled_date=vaccine_date
            )