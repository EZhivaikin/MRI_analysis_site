from .models import Clinic, Patient
from django.conf import settings
from typing import List

class ClinicsManager():
    """
    Domain-model for Clinics
    """
    __clinics = Clinic.objects
    __patients = Patient.objects
    __doctors = settings.AUTH_USER_MODEL.objects

    @staticmethod
    def add_clinic(clinic: Clinic, director: settings.AUTH_USER_MODEL) -> None:
        pass

    @staticmethod
    def add_doctor(clinic: Clinic, doctor: settings.AUTH_USER_MODEL) -> None:
        pass

    @staticmethod
    def add_patient(clinic_id: int, doctor_id: int, card_number: str) -> None:
        pass

    @staticmethod
    def link_doctor_to_clinic(clinic_id: int, doctor_id: int) -> None:
        pass
    
    @staticmethod
    def link_patient_to_clinic(clinic_id: int, patient_id: int) -> None:
        pass
    
    @staticmethod
    def link_patient_to_doctor(doctor_id: int, patient_id: int) -> None:
        pass
    
    @staticmethod
    def get_all_clinics() -> List[Clinic]:
        pass
    
    @staticmethod
    def get_clinics_by_filter(expression) -> List[Clinic]:
        pass
    
    @staticmethod
    def get_doctors_by_clinic(clinic_id: int) -> List[settings.AUTH_USER_MODEL]:
        pass

    @staticmethod
    def get_patients_by_filter(expression) -> List[Patient]:
        pass

    
