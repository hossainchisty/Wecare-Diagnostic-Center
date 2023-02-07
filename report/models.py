# Basic Lib Import
from datetime import date

from django.db import models
from django.urls import reverse

from doctor.models import Doctor
from patient.models import Patient
from utility.common_fields import BaseModel

today = date.today()


class Lab(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referred_by_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Refd By Doctor')
    title = models.CharField(max_length=30)
    report = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date = models.DateField(default=f'{today}')
    STATUS = (
        ('sample', 'Sample Collected'),
        ('completed', 'Completed'),
        ('delivered', 'Delivered'),
    )
    report_status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self) -> str:
        return self.title

    def get_update_url(self):
        return reverse('update_lab',  kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('delete_lab',  kwargs={"pk": self.pk})
