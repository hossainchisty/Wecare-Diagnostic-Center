# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from patient.models import Patient


class UpdatePatient(UpdateView):
    model = Patient
    fields = ['name', 'phone', 'doctor', 'due']
    template_name = 'patient/patient_form.html'
    success_url = reverse_lazy('patient_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this customer.")
        return obj
