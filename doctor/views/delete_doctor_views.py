# Basic Lib Import

from django.shortcuts import redirect
from doctor.models import Doctor


def DeleteDoctor(request, pk):
    ''' Delete an doctor object '''
    if request.method == "POST":
        doctors = Doctor.objects.filter(id=pk)
        doctors.delete()
        return redirect('doctor_list')
