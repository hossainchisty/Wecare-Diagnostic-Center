# Basic Lib Import

from django.shortcuts import redirect, render
from django.views.generic import View

from laboratory.forms.lab_form import LabForm
from laboratory.models import Reportlist


class CreateLabView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'report/add_lab_report.html', {'form': LabForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Lab '''
        form = LabForm(request.POST)
        # Automatically set to the currently logged-in user
        # form.instance.user = request.user
        if form.is_valid():
            value = request.POST.get('report_name')
            reportPrice = Reportlist.objects.get(id=value)
            mainBalance = form.instance.total = reportPrice.price

            doctorBalance = mainBalance - form.instance.referred_by_doctor.commission
            form.instance.referred_by_doctor.total += doctorBalance
            form.save()
            print('Add money')
            """Provide a redirect on GET request."""
            return redirect('lab_report_list')
        else:
            return render(request,  'report/add_lab_report.html', {'form': LabForm()})
