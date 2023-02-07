# Basic Lib Import
from django.contrib.auth.hashers import make_password
from django.db import models

from department.models import Department
from utility.common_fields import BaseModel

# from utility.unique_uuid import unique_code


class Doctor(BaseModel):
    unique_id = models.CharField(max_length=10, null=True, blank=True, editable=False)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    designation = models.CharField(max_length=50)
    depertment = models.ForeignKey(Department, on_delete=models.CASCADE)
    commission = models.CharField(max_length=4, null=True, blank=True, default='0.00')
    total = models.CharField(max_length=4, null=True, blank=True, default='0.00')
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        ''' Encrypted password '''
        self.password = make_password(self.password)
        ''' unique code generator '''
        # self.unique_id = f'{unique_code(6)}'
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class DoctorVisit(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    visit_charges = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.doctor.name
