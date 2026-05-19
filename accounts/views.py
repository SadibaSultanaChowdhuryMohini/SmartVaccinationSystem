from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from vaccination.models import Child
from .forms import RegisterForm, LoginForm
from .models import UserProfile
from .forms import UserProfileForm
def home(request):
    return render(request, 'accounts/home.html')
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'parent'
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                if user.role == 'parent':
                    return redirect('parent_dashboard')
                elif user.role == 'healthworker':
                    return redirect('worker_dashboard')
                else:
                    return redirect('login')
            else:
                return render(request, 'accounts/login.html', {
                    'form': form,
                    'error': 'Invalid username or password'
                })
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def parent_dashboard(request):
    if request.user.role != 'parent':
        return redirect('worker_dashboard')
    children = Child.objects.filter(parent=request.user)
    return render(
        request,
        'accounts/parent_dashboard.html',context={'children': children})

@login_required
def worker_dashboard(request):
    if request.user.role != 'healthworker':
        return redirect('parent_dashboard')
    children = Child.objects.all()
    return render(request,'accounts/worker_dashboard.html',context={'children': children})

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})
@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request,'accounts/edit_profile.html',{'form': form})