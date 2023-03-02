# Basic Lib Import

from django.db import models

from doctor.models import Doctor
from patient.models import Patient
from utility.common_fields import BaseModel
from .reports_models import Reportlist

from laboratory.models.reports_models import *
from laboratory.models.lab_models import *
from patient.models import Patient
from utility.common_fields import BaseModel



class Lab(BaseModel):
    unique_id = models.CharField(max_length=10, null=True, blank=True, editable=False)
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
    duration = models.DateTimeField(help_text='Report Delivery Date-Time', null=True, blank=True)
    note = models.CharField(max_length=60, null=True, blank=True)
    totalBill = models.IntegerField(default=0, null=True)
    totalpayemnt = models.IntegerField(default=0, null=True)

    def __str__(self) -> str:
        return str(self.report_status)


class LabCart(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referred_by_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Refd By Doctor', null=True)

    class Meta:
        verbose_name = 'Lab Cart'


class ReportlistCart(BaseModel):
    title = models.CharField(max_length=30, unique=True)
    commission = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Lab Test'

    def __str__(self) -> str:
        return str(self.title)


class ReportTestinglist(BaseModel):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    commission = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Lab Test'

    def __str__(self) -> str:
        return str(self.title)
