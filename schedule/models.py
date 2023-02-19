# Basic Lib Import
from django.db import models
from django.urls import reverse

from doctor.models import Doctor
from utility.common_fields import BaseModel


class Schedule(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    WEEKDAY_CHOICES = (
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
    )
    weekday = models.CharField(max_length=10, choices=WEEKDAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    appointment_duration = models.CharField(max_length=40)
    visit_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def get_update_url(self):
        return reverse('update_schedule',  kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('delete_schedule',  kwargs={"pk": self.pk})


class Holiday(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.doctor)

    def get_update_url(self):
        return reverse('update_holiday',  kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('delete_holiday',  kwargs={"pk": self.pk})
