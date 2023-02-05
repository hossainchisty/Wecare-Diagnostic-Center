
from django.shortcuts import redirect, render
from django.views import View

from doctor.forms.doctor_visti_form import DoctorVisitForm


class CreateDoctorVisitView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'doctor/add_doctor_visit_charge.html', {'form': DoctorVisitForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Doctor '''
        form = DoctorVisitForm(request.POST)
        # Automatically set to the currently logged-in user
        # form.instance.user = request.user
        if form.is_valid():
            form.save()
            """Provide a redirect on GET request."""
            return redirect('doctor_visit_list')
        else:
            return render(request,  'doctor/add_doctor_visit_charge.html', {'form': DoctorVisitForm()})
