# from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from authenticator.models import User
from doctor.models.doctor_model import Doctor
from utility.helper.decorators.verifiy import EmailBackEnd

# class DoctorSignInView(auth_views.LoginView):
#     ''' Sign in for customer '''
#     form_class = AuthenticationForm
#     template_name = 'authenticator/doctor/login.html'


def DoctorSignInView(request):
    ''' Sign in views '''
    if request.method == 'POST':
        doctor = EmailBackEnd.authenticate(request, mobile_number=request.POST.get('mobile_number'), password=request.POST.get('password')) # noqa
        print(doctor)
    else:
        return render(request, 'authenticator/doctor/login.html')
