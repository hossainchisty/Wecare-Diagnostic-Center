# Basic Lib Import
from django.db import models

from appointment.models import Appointment
from utility.common_fields import BaseModel

from .doctor_model import Doctor


class DoctorVisit(BaseModel):
    """ DoctorVisit model for storing doctor visits charges data """
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    visit_charges = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Doctor Visit'

    def __str__(self):
        return self.doctor.name
