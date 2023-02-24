# Basic Lib Import

from django.shortcuts import redirect
from patient.models import Patient


def DeletePatient(request, pk):
    if request.method == "POST":
        patient = Patient.objects.filter(id=pk)
        patient.delete()
        return redirect('patient_list')
