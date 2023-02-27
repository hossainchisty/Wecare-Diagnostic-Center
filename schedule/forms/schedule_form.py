# Basic Lib Import

from django.forms import ModelForm
from django.forms.widgets import DateInput

from schedule.models import Schedule


class ScheduleForm(ModelForm):
    ''' Form asking for create schedule '''
    class Meta:
        model = Schedule
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'start_time': DateInput(attrs={'type': 'time'}),
            'end_time': DateInput(attrs={'type': 'time'}),
        }
