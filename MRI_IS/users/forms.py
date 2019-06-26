from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from domain.models import Clinic

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # ROLES = [
    #     (1,"Врач"),
    #     (2, "Директор"),
    # ]
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "patronymic",
            "email",
            "phone",
            "password1",
            "password2",
        ]

class ClinicCreationForm(forms.ModelForm):
    class Meta:
        model = Clinic
        exclude = ["director"]