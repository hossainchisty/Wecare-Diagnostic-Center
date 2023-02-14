# Basic Lib Import

from django.db import models

from utility.common_fields import BaseModel


class DiagnosticIncome(BaseModel):
    """ Diagnostic Income model for record company earnings """
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(help_text="Write Your Income Description.", null=True, blank=True)
    sources = models.CharField(max_length=200)

    class Meta:
        ordering = [
            '-created_at'
        ]
        verbose_name = 'Company Income'
        verbose_name_plural = 'Company Income'

    def __str__(self):
        return f"{self.sources} - {self.amount}"
