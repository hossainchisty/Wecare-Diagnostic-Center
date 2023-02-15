# Basic Lib Import
from django.contrib.auth.hashers import make_password
from django.db import models

from department.models import Department
from utility.common_fields import BaseModel


class Doctor(BaseModel):
    """ Doctor model for storing doctor data """
    unique_id = models.CharField(max_length=10, null=True, blank=True, editable=False)
    name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='media/', default='static/img/default.jpg', null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    designation = models.CharField(max_length=50)
    depertment = models.ForeignKey(Department, on_delete=models.CASCADE)
    commission = models.DecimalField(max_digits=5, decimal_places=2,  default=0.00)
    total = models.DecimalField(max_digits=15, decimal_places=2,  default=0.00)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        ''' Build encrypted password '''
        self.password = make_password(self.password)
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
