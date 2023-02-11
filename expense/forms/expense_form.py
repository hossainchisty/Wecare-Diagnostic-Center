# Basic Lib Import

from django.forms import ModelForm
from django.forms.widgets import DateTimeInput

from expense.models import Expense


class ExpenseForm(ModelForm):
    ''' Form asking for create expense '''
    class Meta:
        model = Expense
        fields = ['category', 'date', 'amount', 'note']  # noqa
        widgets = {
            'date': DateTimeInput(attrs={'type': 'date'}),
        }
