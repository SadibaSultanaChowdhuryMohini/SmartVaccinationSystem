from django.shortcuts import render, redirect, get_object_or_404
from .models import Clinic
from .forms import AppointmentForm

TEMPLATE_PATH = 'clinics.html'

def clinic_list(request):
    clinics = Clinic.objects.all()
    context = {
        'page': 'list',
        'clinics': clinics
    }
    return render(request, TEMPLATE_PATH, context)

def clinic_detail(request, clinic_id):
    clinic = get_object_or_404(Clinic, pk=clinic_id)
    context = {
        'page': 'detail',
        'clinic': clinic,
    }
    return render(request, TEMPLATE_PATH, context)

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinic_list')
    else:
        form = AppointmentForm()

    context = {
        'page': 'form',
        'form': form
    }
    return render(request, TEMPLATE_PATH, context)
