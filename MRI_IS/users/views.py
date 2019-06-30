from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView

from domain.clinics_manager import ClinicsManager
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator

from domain.models import Clinic

from .forms import *

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return LoginView.as_view(template_name='users/login.html')(request)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            assign_role(user, 'director')
            messages.success(
                request, 'Вы зарегистрированы! Теперь вы можете войти')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('profile')
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
