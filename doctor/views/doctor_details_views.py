# flake8: noqa
# Basic Lib Import
from doctor.models.doctor_model import Doctor
from django.shortcuts import render, get_object_or_404
from doctor.models.doctor_profit_model import DoctorProfit
from doctor.models.doctor_visits_model import DoctorVisit
from django.db.models import Sum
from django.contrib.humanize.templatetags.humanize import intcomma
from appointment.models import Appointment

def DoctorDetailsView(request, detail_id):
    data = get_object_or_404(Doctor, pk=detail_id)
    ''' Doctor profit amount from lab tests commission '''
    doctor_profit = intcomma(DoctorProfit.objects.filter(id=detail_id).aggregate(Sum('profit'))['profit__sum'])
    ''' Doctor earnings amount from patient visits '''
    patient_visti_amount = intcomma(DoctorVisit.objects.filter(id=detail_id).aggregate(Sum('visit_charges'))['visit_charges__sum'])
    ''' Total appointemnt has been treated '''
    total_appointment = Appointment.objects.filter(doctor=detail_id).count()

    context = {
        "data": data,
        "doctor_profit": doctor_profit,
        "patient_visti_amount": patient_visti_amount,
        'total_appointment' : total_appointment
    }
    return render(request, "doctor/doctor_details.html", context)
