from django.shortcuts import render, redirect
from domain.models import Clinic
from .forms import ClinicCreationForm
from domain.clinics_manager import ClinicsManager
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def clinics_create_edit(request):
    if request.method == 'GET':
        clinic = ClinicsManager.get_clinics_by_director(director=request.user.id)
        if  clinic is None:
            clinic_creation_form = ClinicCreationForm()
            return render(request, 'clinics/create_edit.html',
                          {'clinic_creation_form': clinic_creation_form})
        else:
            clinic_creation_form = ClinicCreationForm(instance=clinic)
            return render(request, 'clinics/create_edit.html',
                          {'clinic_creation_form': clinic_creation_form})
    elif request.method == 'POST':
        form = ClinicCreationForm(request.POST)
        if form.is_valid():
            clinic = form.save(commit=False)
            ClinicsManager.add_clinic(clinic=clinic, director=request.user)
            messages.success(
                request, 'Вы создали клинику!')
            return redirect('profile')