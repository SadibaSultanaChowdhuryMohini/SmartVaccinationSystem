from django.urls import path
from vaccination import views

urlpatterns = [

    path('dashboard/', views.vaccination_dashboard, name='vaccination_dashboard'),
    path('add-child/', views.add_child, name='add_child'),
    path('reminders/', views.vaccination_reminders, name='vaccination_reminders'),
    path('history/', views.vaccination_dashboard, name='vaccination_history'),
]