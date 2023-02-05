# Basic Lib Import
from django.db import models

from doctor.models import Doctor
from utility.common_fields import BaseModel
from utility.unique_uuid import unique_code


class Patient(BaseModel):
    unique_id = models.CharField(max_length=40, null=True, blank=True, editable=False)
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    BLOOD_CHOICES = (
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o-', 'O-'),
        ('o+', 'O-'),
    )
    blood_group = models.CharField(max_length=5, choices=BLOOD_CHOICES, null=True, blank=True)
    patient_age = models.IntegerField(null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    total_bill = models.DecimalField(max_digits=5, decimal_places=2, default='0.00', null=True, blank=True)
    total_deposit = models.DecimalField(max_digits=5, decimal_places=2, default='0.00', null=True, blank=True)
    due = models.DecimalField(max_digits=5, decimal_places=2, default='0.00', null=True, blank=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        ''' unique code generator '''
        # self.unique_id = f'cddc23-{unique_code(6)}'
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
