# Basic Lib Import

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

from appointment.models import Appointment


class MakeAppointmentCancelView(View):
    def get(self, request, id):
        ''' This will cancel an appointment '''
        Appointment.objects.filter(id=id).update(appointment_status='cancelled')
        return HttpResponseRedirect(reverse('appointment_list'))
