from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('profile/',views.profile,name='profile'),
    path('edit-profile/',views.edit_profile,name='edit_profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('parent-dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('worker-dashboard/', views.worker_dashboard, name='worker_dashboard'),
]