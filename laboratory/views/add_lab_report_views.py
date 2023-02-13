# Basic Lib Import

from django.shortcuts import redirect, render
from django.views.generic import View

from doctor.models.doctor_profit_model import DoctorProfit
from laboratory.forms.lab_form import LabForm
from laboratory.models import Reportlist


class CreateLabView(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'report/add_lab_report.html', {'form': LabForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Labratory '''
        form = LabForm(request.POST)
        if form.is_valid():
            elements = request.POST.getlist('report_name')
            rawValue = list(map(int, elements))
            total = 0
            initial = 0
            for item in rawValue:
                reportPrice = Reportlist.objects.get(id=item)
                mainValue = (reportPrice.commission / 100) * reportPrice.price
                initial = initial + mainValue
                print(f'Main Value - {mainValue}')
                total = total + reportPrice.price
                print(f'{reportPrice.price}')
                # print(form.instance.id) FIXME: Output: None
                # addProfit = DoctorProfit.objects.create(
                #     doctor=form.instance.referred_by_doctor,
                #     lab=form.instance.pk,
                #     profit=mainValue
                # )
                # addProfit.save()
            print('total', total)
            form.instance.total = total

            form.save()
            """Provide a redirect on GET request."""
            return redirect('lab_report_list')
        else:
            return render(request,  'report/add_lab_report.html', {'form': LabForm()})
