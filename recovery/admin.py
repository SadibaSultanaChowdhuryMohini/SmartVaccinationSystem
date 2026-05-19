from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(RecoveryPlan)
admin.site.register(ForgotRecoveryPlan)
admin.site.register(SickRecovery)
admin.site.register(TravelRecovery)
admin.site.register(NoSlotRecovery)