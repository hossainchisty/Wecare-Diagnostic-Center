# Basic Lib Import

from django.db import models
from django.urls import reverse

from doctor.models import Doctor
from patient.models import Patient
from utility.common_fields import BaseModel
from .reports_models import Reportlist


class Lab(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referred_by_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Refd By Doctor', null=True, blank=True) # noqa
    report_name = models.ManyToManyField(Reportlist, verbose_name='Report Name', help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.') # noqa
    total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0.00)
    STATUS = (
        ('sample', 'Sample Collected'),
        ('completed', 'Completed'),
        ('delivered', 'Delivered'),
    )
    report_status = models.CharField(max_length=30, choices=STATUS, default='sample')

    def __str__(self) -> str:
        return str(self.report_status)

    def get_update_url(self):
        return reverse('update_lab',  kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('delete_lab',  kwargs={"pk": self.pk})
