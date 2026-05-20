from django.contrib import admin
from .models import Vaccine, Child, VaccinationSchedule


admin.site.register(Vaccine)
admin.site.register(Child)
class VaccinationScheduleAdmin(admin.ModelAdmin):
    list_display = ('child', 'vaccine', 'status')
    list_filter = ('status',)
    search_fields = ('child__name', 'vaccine__name')

admin.site.register(VaccinationSchedule, VaccinationScheduleAdmin)


