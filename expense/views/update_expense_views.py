# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from expense.models import Expense


class UpdateExpense(UpdateView):
    model = Expense
    fields = '__all__'
    template_name = 'expense/expense_form.html'
    success_url = reverse_lazy('manage_expense')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this expense.")
        return obj
