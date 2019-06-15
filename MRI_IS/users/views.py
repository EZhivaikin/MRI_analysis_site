from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator

from domain.models import Clinic

from .forms import *

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            group = form.data.get("user_group")
            user = form.save()
            if group == '1':
                assign_role(user, 'doctor')
            else:
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
    if request.method == 'GET':
        if Clinic.objects.filter(director=request.user.id).count() == 0:
            clinic_creation_form = ClinicCreationForm()
            return render(request, 'users/profile.html', 
                {'clinic_creation_form': clinic_creation_form})
    elif request.method == 'POST':
        form = ClinicCreationForm(request.POST)
        if form.is_valid():
            clinic = form.save(commit=False)
            print(clinic)
            clinic.director = request.user
            clinic.save()
            messages.success(
                request, 'Вы создали клинику!')
            return redirect('login')
    return render(request, 'users/profile.html')
