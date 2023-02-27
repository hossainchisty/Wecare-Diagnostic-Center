# Basic Lib Import

from django.shortcuts import redirect, render
from django.views.generic import View

from appointment.forms.appointment_form import AppointmentForm


class CreateAppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'appointment/add_appointment.html', {'form': AppointmentForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new appointment '''
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            """Provide a redirect on GET request."""
            return redirect('appointment_list')
        else:
            return render(request,  'patient/add_appointment.html', {'form': AppointmentForm()})
