# Basic Lib Import
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View

from expense.models import Category, Expense


class ManageExpense(LoginRequiredMixin, View):
    '''
    List all Expense date expense type and amount.
    '''
    def get(self, request):
        expenses_list = Expense.objects.all().order_by('-id')
        paginator = Paginator(expenses_list, 20)
        page_number = request.GET.get('page')
        expenses = paginator.get_page(page_number)
        context = {
            'expenses': expenses
        }
        return render(request, 'expense/manage_expense.html', context)


class ExpenseCategory(LoginRequiredMixin, View):
    ''' Expense category list '''
    def get(self, request):
        category_list = Category.objects.all().order_by('-id')
        paginator = Paginator(category_list, 20)
        page_number = request.GET.get('page')
        categories = paginator.get_page(page_number)
        context = {
            'categories': categories
        }
        return render(request, 'expense/category_item.html', context)
