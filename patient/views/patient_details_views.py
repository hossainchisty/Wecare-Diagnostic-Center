# flake8: noqa
# Basic Lib Import
# from django.db.models import Sum
# from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from appointment.models import Appointment
from laboratory.models.lab_models import Lab
from patient.models import Patient
from django.core.exceptions import MultipleObjectsReturned
from django.contrib import messages


def PatientDetailsView(request, id, uhid):
    data = get_object_or_404(Patient, unique_id=uhid)
    appointment_completed = Appointment.objects.filter(patient=id, appointment_status='confirmed', payment_status='paid').count()
    lab = Lab.objects.get(patient=id)
    tests = lab.report_name.all()
    context = {
        'tests': tests,
        'lab': lab,
        'data': data,
        'appointment_completed': appointment_completed
    }
    return render(request, "patient/patient_details.html", context)
