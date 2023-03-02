# Basic Lib Import

from django.forms import ModelForm

from laboratory.models.reports_models import Reportlist


class TestForm(ModelForm):
    ''' Form asking for Lab test '''
    class Meta:
        model = Reportlist
        fields = ['title', 'commission', 'price']
