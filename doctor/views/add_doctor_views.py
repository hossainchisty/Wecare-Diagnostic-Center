
from django.shortcuts import redirect, render
from django.views import View

from doctor.forms.doctor_form import DoctorForm
from utility.unique_uuid import unique_code
from authenticator.models import User


class CreateDoctorView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'doctor/add_doctor.html', {'form': DoctorForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Doctor '''
        form = DoctorForm(request.POST)
        name = request.POST.get('name')
        password = request.POST.get('password')
        print('name',name)
        
        email = request.POST.get('email')
        print('email',email)
        # Automatically set to the currently logged-in user
        # form.instance.user = request.user
        user = User(
            first_name=name, last_name=name, username=name, email=email)
        user.set_password(password)
        user.is_doctor = True
        user.save()
        if form.is_valid():
            form.instance.unique_id = f'{unique_code(4)}'
            form.instance.user = user
            form.save()
            """Provide a redirect on GET request."""
            return redirect('doctor_list')
        else:
            return render(request,  'doctor/add_doctor.html', {'form': DoctorForm()})
