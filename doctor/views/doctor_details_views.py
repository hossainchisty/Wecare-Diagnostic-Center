# flake8: noqa
# Basic Lib Import
from doctor.models.doctor_model import Doctor
from django.shortcuts import render, get_object_or_404
from doctor.models.doctor_profit_model import DoctorProfit
from doctor.models.doctor_visits_model import DoctorVisit
from django.db.models import Sum
from django.contrib.humanize.templatetags.humanize import intcomma


def DoctorDetailsView(request, detail_id):
    data = get_object_or_404(Doctor, pk=detail_id)
    doctor_profit = intcomma(DoctorProfit.objects.filter(id=detail_id).aggregate(Sum('profit'))['profit__sum'])
    patient_visti_amount = intcomma(DoctorVisit.objects.filter(id=detail_id).aggregate(Sum('visit_charges'))['visit_charges__sum'])
    context = {
        "data": data,
        "doctor_profit": doctor_profit,
        "patient_visti_amount": patient_visti_amount,
    }
    return render(request, "doctor/doctor_details.html", context)
