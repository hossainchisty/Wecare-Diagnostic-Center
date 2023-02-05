# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from doctor.models import Doctor


class UpdateDoctor(UpdateView):
    model = Doctor
    fields = ['name', 'email', 'phone']
    template_name = 'doctor/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this customer.")
        return obj
