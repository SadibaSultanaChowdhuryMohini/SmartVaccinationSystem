from django.contrib import admin
from .models import Vaccine, Child, VaccinationSchedule


admin.site.register(Vaccine)
admin.site.register(Child)
admin.site.register(VaccinationSchedule)

