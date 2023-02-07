# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from report.models import Lab


class UpdateLabView(UpdateView):
    model = Lab
    fields = ['patient', 'referred_by_doctor', 'report_name', 'report', 'price', 'commission', 'report_status']
    template_name = 'report/lab_report_form.html'
    success_url = reverse_lazy('lab_report_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this customer.")
        return obj
