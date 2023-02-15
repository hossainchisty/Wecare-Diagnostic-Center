# Basic Lib Import

from django.forms import ModelForm

from appointment.models import Appointment


class AppointmentForm(ModelForm):
    ''' Form asking for create appointment '''
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'schedule', 'appointment_status', 'visit_charges',  'remarks', 'discount', 'payment_status'] # noqa