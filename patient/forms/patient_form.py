# Basic Lib Import

from django.forms import ModelForm

from patient.models import Patient

# from django.forms.widgets import DateInput


class PatientForm(ModelForm):
    ''' Form asking for create patient '''
    class Meta:
        model = Patient
        fields = ['name', 'phone', 'gender', 'patient_age', 'doctor', 'status']
        # widgets = {
        #     'date_of_birth': DateInput(attrs={'type': 'date'}),
        # }
