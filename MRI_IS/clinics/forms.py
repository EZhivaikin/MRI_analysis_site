from django import forms
from domain.models import Clinic

class ClinicCreationForm(forms.ModelForm):
    class Meta:
        model = Clinic
        exclude = ["director"]