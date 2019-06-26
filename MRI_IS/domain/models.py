from django.db import models
from django.conf import settings

# Create your models here.


class Clinic(models.Model):
    director = models.IntegerField(unique=True, verbose_name="Директор")
    name = models.CharField(max_length=255, verbose_name="Название клиники")
    contact_address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    BIK = models.CharField(max_length=45, verbose_name="БИК")
    INN = models.CharField(max_length=45, verbose_name="ИНН")


class Patient(models.Model):
    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
    card_number = models.CharField(max_length=45)


class Inspection(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    inspection_date = models.DateTimeField()
    code = models.IntegerField(unique=True)


class Capture(models.Model):
    inspection_code = models.ForeignKey(
        'Inspection',
        to_field='code',
        on_delete=models.CASCADE
    )
    storage_key = models.CharField(max_length=45)
