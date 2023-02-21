# Basic Lib Import
from doctor.models.doctor_model import Doctor
from django.shortcuts import render, get_object_or_404


def DoctorDetailsView(request, detail_id):
    data = get_object_or_404(Doctor, pk=detail_id)
    context = {
        "data": data
    }
    return render(request, "doctor/doctor_details.html", context)
