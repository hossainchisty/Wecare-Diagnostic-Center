# Basic Lib Import
from django.db import models
from django.utils import timezone

from doctor.models import Doctor
from patient.models import Patient
from utility.common_fields import BaseModel


class Appointment(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(default=timezone.now, editable=False)
    STATUS = (
        ('pending confirmation', 'Pending Confirmation'),
        ('confirmed', 'Confirmed'),
        ('treated', 'Treated'),
        ('cancelled', 'Cancelled'),
        ('requested', 'Requested'),
    )
    appointment_status = models.CharField(max_length=40, choices=STATUS, default='pending confirmation')
    visti_description = models.TextField()
    visit_charges = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.IntegerField(null=True, blank=True)
    grand_total = models.DecimalField(max_digits=5, decimal_places=2)
    PAYMENT_TYPE = (
        ('cash', 'Cash'),
        ('card', 'Card')
    )
    deposit_type = models.CharField(max_length=10, choices=PAYMENT_TYPE, null=True, blank=True)
    PAYMENT_STATUS = (
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    )
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS)
    remarks = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        get_latest_by = ['date']

    def __str__(self):
        return self.appointment_status
