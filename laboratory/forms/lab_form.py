# Basic Lib Import
from django.forms import ModelForm

from laboratory.models import Lab


class LabForm(ModelForm):
    ''' Form asking for Lab report '''
    class Meta:
        model = Lab
        fields = ['patient', 'referred_by_doctor', 'report_name'] # noqa
