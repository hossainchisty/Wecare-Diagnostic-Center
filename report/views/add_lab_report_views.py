# Basic Lib Import

from django.shortcuts import redirect, render
from django.views.generic import View

from report.forms.lab_form import LabForm


class CreateLabView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'report/add_lab_report.html', {'form': LabForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Patient '''
        form = LabForm(request.POST)
        # Automatically set to the currently logged-in user
        # form.instance.user = request.user
        if form.is_valid():
            form.save()
            """Provide a redirect on GET request."""
            return redirect('lab_report_list')
        else:
            return render(request,  'report/add_lab_report.html', {'form': LabForm()})
