# Basic Lib Import

from django.forms import ModelForm

from doctor.models import DoctorVisit


class DoctorVisitForm(ModelForm):
    ''' Form asking for create doctor visit '''
    class Meta:
        model = DoctorVisit
        fields = ['doctor', 'visit_charges', 'status']
        # exclude = ['user', ]
