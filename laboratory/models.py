# Basic Lib Import
from datetime import date

from django.db import models
from django.urls import reverse

from doctor.models import Doctor
from patient.models import Patient
from utility.common_fields import BaseModel

today = date.today()


class Reportlist(BaseModel):
    title = models.CharField(max_length=30)
    commission = models.DecimalField(max_digits=5, decimal_places=2,  default=0.00)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Lab Test'

    def __str__(self) -> str:
        return str(self.title)


class Lab(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referred_by_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Refd By Doctor')
    report_name = models.ManyToManyField(Reportlist, verbose_name='Report Name', help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.') # noqa
    report = models.TextField()
    total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)
    date = models.DateField(default=f'{today}')
    STATUS = (
        ('sample', 'Sample Collected'),
        ('completed', 'Completed'),
        ('delivered', 'Delivered'),
    )
    report_status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self) -> str:
        return str(self.report_status)

    def get_update_url(self):
        return reverse('update_lab',  kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('delete_lab',  kwargs={"pk": self.pk})
