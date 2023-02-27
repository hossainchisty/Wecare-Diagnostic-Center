# Basic Lib Import
from datetime import date

from django.db import models

from utility.common_fields import BaseModel

today = date.today()


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Expense(BaseModel):
    """ Expense model for storing expense data """
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date = models.DateField(default=f'{today}') #TODO: REMOVE
    note = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return f"{self.date} - {self.amount}"
