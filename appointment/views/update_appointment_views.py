# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from appointment.models import Appointment


class UpdateAppointment(UpdateView):
    model = Appointment
    fields = '__all__'
    exclue = ['user', ]
    template_name = 'appointment/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this customer.")
        return obj
