# Basic Lib Import

from django.db.models import Sum
from django.shortcuts import redirect, render
from django.views.generic import View

from laboratory.forms.lab_form import LabForm
from laboratory.models import Reportlist


class CreateLabView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'report/add_lab_report.html', {'form': LabForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Labratory '''
        form = LabForm(request.POST)
        # Automatically set to the currently logged-in user
        # form.instance.user = request.user
        if form.is_valid():
            elements = request.POST.getlist('report_name')
            print(elements)
            rawValue = list(map(int, elements))
            print(rawValue)
            for item in rawValue:
                reportPrice = Reportlist.objects.get(id=item)
                # print(sum(reportPrice.price)) # FIXME: 'decimal.Decimal' object is not iterable
                print(f'{reportPrice.title} - {reportPrice.price}')
            form.save()
            """Provide a redirect on GET request."""
            return redirect('lab_report_list')
        else:
            return render(request,  'report/add_lab_report.html', {'form': LabForm()})
