from django.shortcuts import redirect, render
from django.views.generic import View

from doctor.models import Doctor
from frontapp.forms import AppointmentForm
from patient.models import Patient
from schedule.models import Schedule
from utility.unique_uuid import unique_code

# Create your views here.


class Index(View):
    def get(self, request):
        return render(request, 'front/index.html', {'form': AppointmentForm()})

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        doctor = request.POST.get('doctor')
        unique_id = f'{unique_code(6)}'
        doctorID = Doctor.objects.get(id=doctor)

        patientModel = Patient()
        patientModel.name = name
        patientModel.phone = phone
        patientModel.patient_age = age
        patientModel.gender = 'Male'
        patientModel.doctor = doctorID
        patientModel.unique_id = unique_id
        patientModel.save()
        if form.is_valid():
            form.instance.patient = patientModel
            form.instance.visit_charges = 400
            form.instance.grand_total = 700
            form.save()
            """Provide a redirect on GET request."""
            return redirect('index_view')
        else:
            return render(request, 'front/index.html', {'form': AppointmentForm()})


def load_cities(request):
    doctor_id = request.GET.get('doctor')
    schedules = Schedule.objects.filter(doctor_id=doctor_id).order_by('start_time')
    return render(request, 'front/city_dropdown_list_options.html', {'schedules': schedules})


class Appointment(View):
    def get(self, request):
        return render(request, 'front/appointment.html', {'form': AppointmentForm()})

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        doctor = request.POST.get('doctor')
        unique_id = f'cddc23-{unique_code(6)}'

        doctorID = Doctor.objects.get(id=doctor)

        patientModel = Patient()
        patientModel.name = name
        patientModel.phone = phone
        patientModel.patient_age = age
        patientModel.gender = 'Male'
        patientModel.doctor = doctorID
        patientModel.unique_id = unique_id
        patientModel.save()
        if form.is_valid():
            form.instance.patient= patientModel
            form.instance.visit_charges = 400 
            form.instance.grand_total = 700 
            form.save()
            """Provide a redirect on GET request."""
            return redirect('appointment_view')
        else:
            return render(request,  'front/appointment.html', {'form': AppointmentForm()})


class About(View):
    def get(self, request):
        return render(request, 'front/index.html')


class Contact(View):
    def get(self, request):
        return render(request, 'front/contact.html')


class Price(View):
    def get(self, request):
        return render(request, 'front/price.html')


class Service(View):
    def get(self, request):
        return render(request, 'front/service.html')


class Team(View):
    def get(self, request):
        return render(request, 'front/team.html')


class Testimonial(View):
    def get(self, request):
        return render(request, 'front/testimonial.html')
