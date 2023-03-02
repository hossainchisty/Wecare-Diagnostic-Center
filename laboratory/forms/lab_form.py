# Basic Lib Import
from django.forms import ModelForm
from django import forms
from laboratory.models.lab_models import Lab


class LabForm(ModelForm):
    ''' Form asking for Lab report '''
    class Meta:
        model = Lab
        fields = ['patient', 'referred_by_doctor', 'report_name', 'duration'] # noqa
        widgets = {
            'duration': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
