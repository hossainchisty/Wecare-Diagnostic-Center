
from django.shortcuts import redirect, render
from django.views import View

from doctor.forms.doctor_form import DoctorForm
from utility.unique_uuid import unique_code


class CreateDoctorView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'doctor/add_doctor.html', {'form': DoctorForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Doctor '''
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.instance.unique_id = f'{unique_code(4)}'
            form.save()
            """Provide a redirect on GET request."""
            return redirect('doctor_list')
        else:
            return render(request,  'doctor/add_doctor.html', {'form': DoctorForm()})
