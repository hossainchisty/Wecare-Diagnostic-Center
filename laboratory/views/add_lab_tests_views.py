# Basic Lib Import

from django.shortcuts import redirect, render
from django.views.generic import View

from laboratory.forms.tests_form import TestForm


class CreateTestView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'report/add_lab_tests.html', {'form': TestForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new test '''
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            """Provide a redirect on GET request."""
            return redirect('lab_tests_list')
        else:
            return render(request,  'report/add_lab_tests.html', {'form': TestForm()})
