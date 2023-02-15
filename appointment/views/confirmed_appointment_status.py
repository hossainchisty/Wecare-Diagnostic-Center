# Basic Lib Import

from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

from appointment.models import Appointment
from doctor.models.doctor_model import Doctor
from doctor.models.doctor_visits_model import DoctorVisit


class MakeAppointmentConfirmedView(View):
    def get(self, request, id):
        ''' This will confirmed an appointment '''
        Appointment.objects.filter(id=id).update(appointment_status='confirmed', payment_status='paid')
        getID = Appointment.objects.get(id=id)
        doctorConfirmed = DoctorVisit.objects.create(
            doctor=getID.doctor,
            appointment=getID,
            visit_charges=getID.visit_charges,
        )
        doctorConfirmed.save()
        with transaction.atomic():
            ''' Calculate total doctor amount '''
            amount = getID.doctor.total
            total_amount = amount + getID.visit_charges
            Doctor.objects.update(total=total_amount)
            return HttpResponseRedirect(reverse('appointment_list'))
