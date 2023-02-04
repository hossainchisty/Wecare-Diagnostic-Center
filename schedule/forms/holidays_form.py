# Basic Lib Import

from django.forms import ModelForm
from django.forms.widgets import DateInput

from schedule.models import Holiday


class HolidaysForm(ModelForm):
    ''' Form asking for create holidays '''

    class Meta:
        model = Holiday
        fields = ['doctor', 'date']
        # exclude = ['user', ]
        widgets = {'date': DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control',
                                                                 'placeholder': 'Select a date', 'type': 'date'
                }),} # noqa
