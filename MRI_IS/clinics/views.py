from django.shortcuts import render, redirect
from domain.models import Clinic
from users.models import User
from .forms import ClinicCreationForm
from users.forms import UserRegisterForm, UserCreationForm
from domain.clinics_manager import ClinicsManager
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import View, CreateView, UpdateView
from rolepermissions.roles import assign_role

# Create your views here.

# TODO: rewrite to class-based view


def clinics_create_edit(request):
    if request.method == 'GET':
        clinic = ClinicsManager.get_clinics_by_director(
            director=request.user.id)
        if clinic is None:
            clinic_creation_form = ClinicCreationForm()
            return render(request, 'clinics/create_edit.html',
                          {'clinic_creation_form': clinic_creation_form,
                           'action': 'Создать'})
        else:
            clinic_creation_form = ClinicCreationForm(instance=clinic)
            return render(request, 'clinics/create_edit.html',
                          {'clinic_creation_form': clinic_creation_form,
                           'action': 'Изменить'})
    elif request.method == 'POST':
        clinic = ClinicsManager.get_clinics_by_director(
            director=request.user.id)
        form = ClinicCreationForm(request.POST, instance=clinic)
        if form.is_valid():
            clinic = form.save(commit=False)
            clinic = ClinicsManager.create_edit_clinic(
                clinic=clinic, director=request.user)
            messages.success(
                request, 'Вы создали клинику!')
            return redirect('doctors-list')


class DoctorListView(ListView):

    model = User
    paginate_by = 10
    template_name = "doctors/list.html"
    ordering = ['-created']

    def get_queryset(self):
        clinic = ClinicsManager.get_clinics_by_director(
            director=self.request.user.id)
        queryset = User.objects.filter(clinic_id=clinic.id)
        return queryset


# TODO: find more accurate way
class DoctorCreateEdit(View):
    template_name = "doctors/create_edit.html"
    form_class = UserRegisterForm
    model = User

    def get(self, request, *args, **kwargs):
        if(kwargs['doctor_id'] != 0):
            doctor = User.objects.get(id=kwargs['doctor_id'])
            doctor_form = self.form_class(instance=doctor)
            return render(request, self.template_name, {'doctor_form': doctor_form, "action": "Изменить"})
        else:
            doctor_form = self.form_class()
            return render(request, self.template_name, {'doctor_form': doctor_form, "action": "Добавить"})

    def post(self, request, *args, **kwargs):
        if(kwargs['doctor_id'] != 0):
            doctor = User.objects.get(id=kwargs['doctor_id'])
            form = self.form_class(request.POST, instance=doctor)
            if form.is_valid():
                doctor = form.save(commit=False)
                doctor.clinic_id = request.user.clinic_id
                doctor.save()
                assign_role(doctor, 'doctor')
                messages.success(
                    request, 'Вы добавили доктора!')
        else:
            form = self.form_class(request.POST)
            doctor = form.save(commit=False)
            doctor.clinic_id = request.user.clinic_id
            doctor.save()
            assign_role(doctor, 'doctor')
        return redirect('doctors-list')
