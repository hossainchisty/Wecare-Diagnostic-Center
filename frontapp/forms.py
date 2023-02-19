from django import forms
# from .models import Person, City
from doctor.models import Doctor
from schedule.models import Schedule
from appointment.models import Appointment
from django.forms import ModelForm, TextInput, EmailInput


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('doctor', 'schedule')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['schedule'].queryset = Schedule.objects.none()

        if 'doctor' in self.data:
            try:
                doctor_id = int(self.data.get('doctor'))
                self.fields['schedule'].queryset = Schedule.objects.filter(doctor_id=doctor_id).order_by('appointment')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['schedule'].queryset = self.instance.doctor.schedule_set.order_by('appointment')
