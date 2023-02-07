# Basic Lib Import

from django.forms import ModelForm

from report.models import Lab


class LabForm(ModelForm):
    ''' Form asking for create patient '''
    class Meta:
        model = Lab
        fields = ['patient', 'referred_by_doctor', 'report_name', 'report', 'price', 'commission', 'date', 'report_status'] # noqa
