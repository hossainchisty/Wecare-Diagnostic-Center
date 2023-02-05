# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from doctor.models import DoctorVisit


class UpdateDoctorVisit(UpdateView):
    model = DoctorVisit
    fields = ['doctor', 'visit_charges']
    template_name = 'doctor/doctor_visit_charge_form.html'
    success_url = reverse_lazy('doctor_visit_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this customer.")
        return obj
