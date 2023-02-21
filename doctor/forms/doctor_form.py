# Basic Lib Import
from django import forms
# from django.db import transaction
from django.forms import ModelForm

from doctor.models import Doctor


class DoctorForm(ModelForm):
    ''' Form asking for create doctor '''
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Doctor
        fields = ['name', 'email', 'password', 'phone', 'designation', 'depertment', 'avatar']
        widgets = {
            'password': forms.PasswordInput(),
         }

#     def __init__(self, *args, **kwargs):
#         super(DoctorForm, self).__init__(*args, **kwargs)

#     @transaction.atomic
#     def save(self):
#         print('Comming......')
#         user = super().save(commit=False)
#         print(f'User {user}')
#         user.is_doctor = True
#         print(f'{user.is_doctor}')
#         user.save()
#         # FIXME: "Doctor.user" must be a "User" instance.
#         doctor = Doctor.objects.create(user=user)
#         doctor.name = self.cleaned_data.get('name')
#         doctor.email = self.cleaned_data.get('email')
#         doctor.password = self.cleaned_data.get('password')
#         doctor.phone = self.cleaned_data.get('phone')
#         doctor.designation = self.cleaned_data.get('designation')
#         doctor.depertment = self.cleaned_data.get('depertment')
#         doctor.avatar = self.cleaned_data.get('avatar')
#         doctor.save()
#         return doctor
