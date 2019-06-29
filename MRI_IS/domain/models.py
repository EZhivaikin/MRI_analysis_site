from django.db import models
from django.conf import settings

# Create your models here.


class Clinic(models.Model):
    director = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Директор",
        on_delete=models.CASCADE
    )
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


class Bill(models.Model):
    bill_number = models.IntegerField()
    bill_data = models.DateTimeField()
    payment_date = models.DateTimeField()
    is_payed = models.BooleanField()
    status_description = models.CharField(max_length=255)
    amount = models.FloatField()
    bill_status = models.IntegerField()


class Payment(models.Model):
    purpose = models.CharField(max_length=255)
    BIK = models.CharField(max_length=255)
    INN = models.CharField(max_length=255)
    amount = models.FloatField()
    bill_date = models.DateField()
    clinic_id = models.IntegerField()  # TODO: foreign key
    bill_number = models.IntegerField()
    operation_status = models.IntegerField()


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    transactions_price = models.CharField(max_length=255)


class TariffsService(models.Model):
    tariff_id = models.IntegerField()  # TODO: foreign key
    service_id = models.IntegerField()  # TODO: foreign key
    transactions_count = models.IntegerField()


class ClinicsTariff(models.Model):
    tariff_id = models.IntegerField()  # TODO: foreign key
    clinic_id = models.IntegerField()  # TODO: foreign key
    date_start = models.DateField()  # TODO: durationField
    date_end = models.DateField()


class TransactionsLeftover(models.Model):
    clinic_id = models.IntegerField()  # TODO: foreign key
    service_id = models.IntegerField()  # TODO: foreign key
    transactions_left = models.IntegerField()


class Tariff(models.Model):
    request_count = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    is_enabled = models.BooleanField()
    description = models.CharField(max_length=255)
    duration = models.IntegerField()
