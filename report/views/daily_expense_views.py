# Basic Lib Import

from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from django.shortcuts import render
from django.views.generic import View

from expense.models import Expense


class DailyExpense(LoginRequiredMixin, View):
    ''' List all daily expense report. '''
    def get(self, request):
        daily_expense = Expense.objects.all().annotate(date_month=ExtractMonth('date'))

        init_date = datetime.date(datetime.now()-timedelta(days=365))
        print(init_date)
        ends_date = datetime.date(datetime.now())
        print(ends_date)
        monthly = Expense.objects.filter(date__range=(init_date, ends_date)).values('date__month').aggregate(amount=Sum('amount')) # noqa
        today = datetime.now()
        print(today.strftime('%B'))
        print(f'{daily_expense=}')
        print(f'{monthly=}')
        context = {
            'daily_expense': daily_expense
        }
        return render(request, 'report/daily_expense_report.html', context)
