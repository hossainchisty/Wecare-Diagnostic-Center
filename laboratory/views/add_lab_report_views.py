# flake8: noqa
# Basic Lib Import

from django.db import transaction
from django.shortcuts import redirect, render
from django.views.generic import View

from doctor.models.doctor_profit_model import DoctorProfit
from income.models import DiagnosticIncome
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
            totalProfit = 0
            initialCommission = 0
            diagnosticProfit = 0
            for item in rawValue:
                with transaction.atomic():
                    ''' if your program crashes, the database guarantees that either all the changes will be applied, or none of them.
                    '''
                    reportPrice = Reportlist.objects.get(id=item)
                    ''' Get doctor commission from tests '''
                    totalCommission = (reportPrice.commission / 100) * reportPrice.price
                    initialCommission = initialCommission + totalCommission
                    totalProfitAmount = totalProfit + initialCommission
                    total = total + reportPrice.price
                    ''' Get total diagnostic income '''
                    diagnosticProfit = total - totalProfitAmount
                form.instance.total = total
                formObject = form.save()
                ''' Adding diagnostic total profit from tests '''
                addDiagnosticAmount = DiagnosticIncome.objects.create(
                    amount=diagnosticProfit,
                    sources='Earning from lab tests',
                )
                addDiagnosticAmount.save()
                ''' Adding doctor total profit from commission '''
                addProfit = DoctorProfit.objects.create(
                            doctor=form.instance.referred_by_doctor,
                            lab=formObject,
                            profit=totalProfitAmount
                            )
                addProfit.save()
                """Provide a redirect on GET request."""
                return redirect('lab_report_list')
            else:
                return render(request,  'report/add_lab_report.html', {'form': LabForm()})
