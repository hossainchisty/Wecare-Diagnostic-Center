# Basic Lib Import

from django.forms import ModelForm

from expense.models import Expense


class ExpenseForm(ModelForm):
    ''' Form asking for create expense '''
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'note']
