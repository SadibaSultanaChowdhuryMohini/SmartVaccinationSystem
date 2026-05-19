from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('parent', 'Parent'),
        ('healthworker', 'Health Worker'),
    )
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='parent')
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    health_worker_id = models.CharField(max_length=100, blank=True, null=True)
    is_verified_worker = models.BooleanField(default=False)
    def _str_(self):
        return self.username

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('parent', 'Parent'),
        ('healthworker', 'Health Worker'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20,blank=True)
    address = models.TextField(blank=True)
    def _str_(self):
        return self.user.username