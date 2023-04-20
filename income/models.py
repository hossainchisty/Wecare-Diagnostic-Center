# Basic Lib Import

from django.db import models
from django.utils.timezone import now

from laboratory.models.lab_models import Lab

class CompanyIncome(models.Model):
    """ Diagnostic Income model for record company earnings """
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(help_text="Write Your Income Description.", null=True, blank=True)
    sources = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name = 'Company Income'
        verbose_name_plural = 'Company Income'

    def __str__(self):
        return f"{self.sources} - {self.amount}"
