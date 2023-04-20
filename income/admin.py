from django.contrib import admin

from income.models import CompanyIncome


@admin.register(CompanyIncome)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'sources')
