from django.contrib import admin
from .models import Vaccine, Child, VaccinationSchedule, VaccinationReminder


admin.site.register(Vaccine)
admin.site.register(Child)
admin.site.register(VaccinationSchedule)
admin.site.register(VaccinationReminder)
