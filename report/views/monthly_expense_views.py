# Basic Lib Import
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View

from expense.models import Expense


class MonthlyExpense(LoginRequiredMixin, View):
    ''' List all monthly expense report. '''
    def get(self, request):
        expenses_list = Expense.objects.all().order_by('-id')
        paginator = Paginator(expenses_list, 20)
        page_number = request.GET.get('page')
        expenses = paginator.get_page(page_number)
        context = {
            'expenses': expenses
        }
        return render(request, 'report/monthly_expense_report.html', context)
