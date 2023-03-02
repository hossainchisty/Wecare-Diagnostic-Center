# Basic Lib Import
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import View

from doctor.models.doctor_profit_model import DoctorProfit
from expense.models import Expense
# from income.models import DiagnosticIncome


class FinancialReportView(LoginRequiredMixin, View):
    ''' List all financial report. '''
    def get(self, request):
        doctor_profit = intcomma(DoctorProfit.objects.aggregate(Sum('profit'))['profit__sum'])
        # gross_income = intcomma(DiagnosticIncome.objects.aggregate(Sum('amount'))['amount__sum'])
        total_expense = intcomma(Expense.objects.aggregate(Sum('amount'))['amount__sum'])
        context = {
            'doctor_profit': doctor_profit,
            # 'gross_income': gross_income,
            'total_expense': total_expense,
        }
        return render(request, 'report/financial_report.html', context)
