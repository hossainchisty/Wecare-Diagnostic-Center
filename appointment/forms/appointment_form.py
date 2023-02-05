# Basic Lib Import

from django.forms import ModelForm
from django.forms.widgets import DateTimeInput

from appointment.models import Appointment


class AppointmentForm(ModelForm):
    ''' Form asking for create appointment '''
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'appointment_status', 'visit_charges',  'remarks', 'discount', 'grand_total', 'payment_status']  # noqa
        widgets = {
            'date': DateTimeInput(attrs={'type': 'date'}),
        }
