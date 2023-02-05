# Basic Lib Import

# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from doctor.models import Doctor


class DeleteDoctor(DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctor_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to delete this customer.")
        return obj
