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

    def save(self, commit=True):
        instance = super(UserRegisterForm, self).save(commit=False)
        instance.clinic_id = 0
        instance.save()
        return instance


class ClinicCreationForm(forms.ModelForm):
    class Meta:
        model = Clinic
        exclude = ["director"]
