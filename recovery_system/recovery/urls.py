from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.recovery_list,name='recovery_list'),
    path('create/',views.create_recovery,name='create_recovery'),
    path('update/<int:id>/',views.update_recovery,name='update_recovery'),
    path('delete/<int:id>/',views.delete_recovery,name='delete'),
]