# Basic Lib Import
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from expense.models import Category, Expense


@admin.register(Expense)
class ExpenseAdmin(ImportExportModelAdmin):
    list_display = ('category', 'date', 'amount')


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name',)
