# Basic Lib Import
from django.db import models

from utility.common_fields import BaseModel


class Reportlist(BaseModel):
    title = models.CharField(max_length=30)
    commission = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Lab Test'

    def __str__(self) -> str:
        return str(self.title)
