# Basic Lib Import
from django.shortcuts import redirect

from expense.models import Expense


def DeleteExpense(request, pk):
    ''' Delete an expense object '''
    if request.method == "POST":
        expense = Expense.objects.filter(id=pk)
        expense.Delete()
        return redirect('manage_expense')
