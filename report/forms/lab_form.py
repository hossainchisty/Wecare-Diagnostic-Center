# Basic Lib Import

from django.forms import ModelForm

from report.models import Lab

# from django.forms.widgets import DateInput


class LabForm(ModelForm):
    ''' Form asking for create patient '''
    class Meta:
        model = Lab
        fields = ['patient', 'referred_by_doctor', 'report_name', 'report', 'price', 'commission', 'date', 'report_status']
        # widgets = {
        #     'date_of_birth': DateInput(attrs={'type': 'date'}),
        # }
