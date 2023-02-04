# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from department.models import Department


class UpdateDepartment(UpdateView):
    model = Department
    fields = ['department_name', 'status']
    template_name = 'department/department_form.html'
    success_url = reverse_lazy('department_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this customer.")
        return obj
