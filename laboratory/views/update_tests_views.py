# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from laboratory.models.reports_models import Reportlist


class UpdateTest(UpdateView):
    model = Reportlist
    fields = '__all__'
    template_name = 'report/tests_form.html'
    success_url = reverse_lazy('lab_tests_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this expense.")
        return obj
