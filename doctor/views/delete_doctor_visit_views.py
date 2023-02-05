# Basic Lib Import

# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from doctor.models import DoctorVisit


class DeleteDoctorVisit(DeleteView):
    model = DoctorVisit
    success_url = reverse_lazy('doctor_visit_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to delete this customer.")
        return obj
