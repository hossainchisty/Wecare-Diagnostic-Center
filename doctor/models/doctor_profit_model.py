# Basic Lib Import

from django.db import models

from laboratory.models import Lab
from utility.common_fields import BaseModel

from .doctor_model import Doctor


class DoctorProfit(BaseModel):
    """ DoctorProfit model for storing doctor profits data """
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    profit = models.DecimalField(max_digits=5, decimal_places=2,  default=0.00)

    class Meta:
        verbose_name = 'Doctor Profit'

    def __str__(self) -> str:
        return str(self.doctor)
