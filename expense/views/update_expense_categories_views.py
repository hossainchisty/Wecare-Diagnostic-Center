# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from expense.models import Category


class UpdateExpenseCategories(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'expense/categories_form.html'
    success_url = reverse_lazy('expense_category')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this expense.")
        return obj
