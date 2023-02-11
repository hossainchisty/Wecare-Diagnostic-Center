# Basic Lib Import
import datetime
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
    YEAR_CHOICES = [(y, y) for y in range(2000, datetime.date.today().year+1)]
    MONTH_CHOICE = [(m, m) for m in range(1, 13)]

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date = models.DateField(default=f'{today}')
    note = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    month = models.IntegerField(choices=MONTH_CHOICE, default=datetime.datetime.now().month)

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return f"{self.date} - {self.amount}"
