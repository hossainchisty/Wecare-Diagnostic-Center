# Basic Lib Import

from django.forms import ModelForm

from doctor.models import Doctor


class DoctorForm(ModelForm):
    ''' Form asking for create doctor '''
    class Meta:
        model = Doctor
        fields = ['name', 'email', 'password', 'phone', 'designation', 'depertment', 'avatar', 'status']
        # exclude = ['user', ]
