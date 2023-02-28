# Basic Lib Import
from expense.models import Category
from django.shortcuts import redirect


def DeleteExpenseCategories(request, pk):
    ''' Delete an expense category object '''
    if request.method == "POST":
        expense_category = Category.objects.filter(id=pk)
        expense_category.Delete()
        return redirect('expense_category')
