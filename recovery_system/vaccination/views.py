from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Child, VaccinationSchedule
from .forms import ChildRegistrationForm


@login_required
def vaccination_dashboard(request):

    children = Child.objects.filter(parent=request.user)


    upcoming_schedules = VaccinationSchedule.objects.filter(
        child__parent=request.user,
        is_completed=False
    ).order_by('scheduled_date')


    vaccination_history = VaccinationSchedule.objects.filter(
        child__parent=request.user,
        is_completed=True
    ).order_by('-completed_date')

    return render(request, 'vaccination/dashboard.html', {
        'children': children,
        'schedules': upcoming_schedules,
        'history': vaccination_history
    })


@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST)
        if form.is_valid():
            child_profile = form.save(commit=False)
            child_profile.parent = request.user
            child_profile.save()
            return redirect('vaccination_dashboard')
    else:
        form = ChildRegistrationForm()

    return render(request, 'vaccination/add_child.html', {'form': form})


@login_required
def vaccination_reminders(request):

    schedules = VaccinationSchedule.objects.filter(child__parent=request.user, is_completed=False)
    return render(request, 'vaccination/vaccination_reminders.html', {'schedules': schedules})