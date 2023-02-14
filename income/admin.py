from django.contrib import admin

from income.models import DiagnosticIncome


@admin.register(DiagnosticIncome)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'sources')
