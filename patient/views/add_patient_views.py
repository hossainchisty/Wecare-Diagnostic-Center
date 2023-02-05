# Basic Lib Import

from django.shortcuts import redirect, render
from django.views.generic import View

from patient.forms.patient_form import PatientForm
from utility.unique_uuid import unique_code


class CreatePatientView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'patient/add_patient.html', {'form': PatientForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Patient '''
        form = PatientForm(request.POST)
        # Automatically set to the currently logged-in user
        # form.instance.user = request.user
        if form.is_valid():
            # Save the patient unique id example: cddc23-356782 .
            form.instance.unique_id = f'cddc23-{unique_code(6)}'
            form.save()
            """Provide a redirect on GET request."""
            return redirect('patient_list')
        else:
            return render(request,  'patient/add_patient.html', {'form': PatientForm()})
