from django.shortcuts import render,redirect
from .models import RecoveryPlan
from .forms import RecoveryForm

def recovery_list(request):
    recoveries = RecoveryPlan.objects.all()
    return render(request,'recovery/recovery_list.html',context={'recoveries': recoveries})

def create_recovery(request):
    if request.method == 'POST':
        form = RecoveryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recovery_list')
    else:
        form = RecoveryForm()
    return render(request,'recovery/create_recovery.html',context = {'form':form})

def update_recovery(request, id):
    recovery = RecoveryPlan.objects.get(id=id)
    if request.method == 'POST':
        form = RecoveryForm(
            request.POST,
            request.FILES,
            instance=recovery
        )
        if form.is_valid():
            form.save()
            return redirect('recovery_list')
    else:
        form = RecoveryForm( instance=recovery)
    return render(request,'recovery/create_recovery.html',context = {'form': form})
def delete_recovery(request, id):
    recovery = RecoveryPlan.objects.get(id=id)
    recovery.delete()
    return redirect('recovery_list')