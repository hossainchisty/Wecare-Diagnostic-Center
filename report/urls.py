# Basic Lib Import
from django.urls import path

from report.views.daily_expense_views import DailyExpense
from report.views.medical_report_views import MedicalReport
from report.views.monthly_expense_views import MonthlyExpense

# Routing Implement
urlpatterns = [
    # Expense Report
    path('daily/expense/', DailyExpense.as_view(), name='daily_expense'),
    path('monthly/expense/', MonthlyExpense.as_view(), name='monthly_expense'),
    path('medical/report', MedicalReport.as_view(), name='medical_report'),
]
