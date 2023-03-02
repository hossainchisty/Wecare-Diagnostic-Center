# Basic Lib Import
from django.db import models

from doctor.models import Doctor
from utility.common_fields import BaseModel


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
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, default='0.00', null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=2, default='0.00', null=True, blank=True)
    due = models.DecimalField(max_digits=15, decimal_places=2, default='0.00', null=True, blank=True)
    discount = models.IntegerField(default=0)
    PAYMENT_TYPE = (
        ('cash', 'Cash'),
        ('card', 'Card')
    )
    deposit_type = models.CharField(max_length=10, choices=PAYMENT_TYPE, null=True, blank=True)
    PAYMENT_STATUS = (
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('due', 'Due')
    )
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='unpaid')
    remarks = models.CharField(max_length=20, null=True, blank=True)
    # TODO: received_by
    status = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     ''' update payment status '''
    #     if self.due == 0.00:
    #         self.payment_status == 'paid'
    #     else:
    #         self.payment_status == 'unpaid'
    #     super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
