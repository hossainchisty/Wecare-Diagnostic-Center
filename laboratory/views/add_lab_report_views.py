# flake8: noqa
# Basic Lib Import

from django.db import transaction
from django.shortcuts import redirect, render
from django.views.generic import View

from doctor.models.doctor_profit_model import DoctorProfit
from income.models import CompanyIncome
from laboratory.forms.lab_form import LabForm
from laboratory.models import Reportlist
from doctor.models.doctor_model import Doctor
from patient.models import Patient
from utility.unique_uuid import unique_code

from django.http import JsonResponse
from laboratory.models import *
from laboratory.models.lab_models import *
from laboratory.models.reports_models import *
import json
from utility.unique_uuid import unique_code
from decimal import Decimal


def lab_bill_pay(request):
    
    bill_pay = request.POST['bill_pay']
    totalBill = request.POST['totalBill']
    totalProfitAmountbyDoctor = request.POST['totalProfitAmountbyDoctor']
    diagnosticProfit = request.POST['diagnosticProfit']

    labCart = LabCart.objects.all().first()
    reportlist = ReportlistCart.objects.all()

    lab = Lab()
    lab.unique_id = f'{unique_code(10)}'
    lab.patient = labCart.patient
    lab.referred_by_doctor = labCart.referred_by_doctor
    lab.totalBill = totalBill
    lab.totalpayemnt = bill_pay
    lab.save()

    
    
    for reportlist in reportlist:
        reportTestinglist = ReportTestinglist()
        reportTestinglist.lab = lab
        reportTestinglist.title = reportlist.title
        reportTestinglist.price = reportlist.price
        reportTestinglist.commission = reportlist.commission
        reportTestinglist.save()
     

    addDiagnosticAmount = CompanyIncome.objects.create(
                    lab=lab,
                    amount=diagnosticProfit,
                    description=f'The revenue estimated was {diagnosticProfit} Taka.',
                    sources='The revenue generated from clinical laboratory services.',
                )
    addDiagnosticAmount.save()

    addProfit = DoctorProfit.objects.create(
                            lab=lab,
                            doctor=labCart.referred_by_doctor,
                            profit=totalProfitAmountbyDoctor
                            )
    addProfit.save()

    doctor = Doctor.objects.get(id=addProfit.doctor.id)
    
    totalProfitAmountbyDoctor_af = Decimal(totalProfitAmountbyDoctor)

    total_amount = totalProfitAmountbyDoctor_af + doctor.total

    print('total_amount total_amount total_amount',total_amount)

    Doctor.objects.filter(id=addProfit.doctor.id).update(total=total_amount)

    patient = Patient.objects.get(id=lab.patient.id)

    patient_before_total_af = Decimal(lab.totalBill)
    patient_before_total = patient_before_total_af
    patient_total = patient_before_total +  patient.grand_total

    patient_before_paid_amount_af = Decimal( bill_pay)
    patient_before_paid_amount = patient_before_paid_amount_af 
    patient__paid_amount = patient_before_paid_amount +  patient.paid_amount


    Patient.objects.filter(id=lab.patient.id).update(grand_total=patient_total)
    Patient.objects.filter(id=lab.patient.id).update(paid_amount=patient__paid_amount)


    ReportlistCart.objects.all().delete()
    LabCart.objects.all().delete()  


    print('bill_pay',bill_pay)

    return redirect('dashboard')


def newCartReport(request):
    report_id = request.POST['report_id']
    newCommision_number = request.POST['newCommision_number']

    reportlist = Reportlist.objects.get(id=report_id)


    if len(newCommision_number) == 0:
        reportlistCart = ReportlistCart()
        reportlistCart.title = reportlist.title
        reportlistCart.price = reportlist.price
        reportlistCart.commission = reportlist.commission
        reportlistCart.save()
    else:
        reportlistCart = ReportlistCart()
        reportlistCart.title = reportlist.title
        reportlistCart.price = reportlist.price
        reportlistCart.commission = newCommision_number
        reportlistCart.save()

    print('report_id',report_id)
    print('newcart_number',newCommision_number)
    return redirect('lab_cart')

def labCart(request):

    tests = ReportlistCart.objects.all().order_by('-id')
    totalreportlistCart = ReportlistCart.objects.all().order_by('-id')

    totalCommission = 0
    totalPrice = 0
    totalBill = 0
    totalProfit = 0
    initialCommission = 0

    for totalreportlistCart in totalreportlistCart:
        totalPrice = totalPrice + totalreportlistCart.price
        totalCommission = (totalreportlistCart.commission / 100) * totalreportlistCart.price
        initialCommission = initialCommission + totalCommission
        totalProfitAmountbyDoctor = totalProfit + initialCommission
        totalBill = totalBill + totalreportlistCart.price

    diagnosticProfit = totalBill - totalProfitAmountbyDoctor


        # print(totalreportlistCart.price)

    labCart = LabCart.objects.all().first()
    reportlist = Reportlist.objects.all()

    data = {
        'tests': tests,
        'totalCommission': totalCommission,
        'totalPrice': totalPrice,
        'totalProfitAmountbyDoctor': totalProfitAmountbyDoctor,
        'totalBill': totalBill,
        'diagnosticProfit': diagnosticProfit,
        'labCart': labCart,
        'reportlist': reportlist,
        }

    return render(request,  'report/lab_cart.html', data)



# totalCommission = (reportPrice.commission / 100) * reportPrice.price
#                         initialCommission = initialCommission + totalCommission
#                         totalProfitAmount = totalProfit + initialCommission
#                         total = total + reportPrice.price

def load_more_content(request):
    offset = request.GET.get('offset')
    # Use the offset parameter to get the next set of content from the database or another source
    # Build the HTML for the new content
    content_html = '<div>New content here</div>'
    print('sdfgdsgf')
    myreport =Reportlist.objects.get(id=offset)

    report_test_list = {'id':myreport.id,'title':myreport.title,'commission':myreport.commission,'price':myreport.price}


    print(report_test_list)
    data = {
        'content_html': content_html,
        'my': offset,
        'report_test_list': report_test_list,
    }

    return JsonResponse({'data': data})



class CreateLabView(View):
    def get(self, request, *args, **kwargs):
        ReportlistCart.objects.all().delete()
        LabCart.objects.all().delete()
        patient_list = Patient.objects.all().order_by('-id')
        doctor_list = Doctor.objects.all().order_by('-id')
        report_list = Reportlist.objects.all().order_by('-id')
        data = {
        'doctor_list': doctor_list,
        'patient_list': patient_list,
        'report_list': report_list,
    }
        return render(request,  'report/add_lab_report.html', data)

    def post(self, request, *args, **kwargs):
        ''' Create a new Labratory '''

        lab_name = request.POST['lab_name']



        # print('bbbbbbbb',lab_name)
        # print(type(lab_name))

        if lab_name == "patient":
            print('ffff')
            patient_add = Patient()
            patient_add.name = request.POST['patient_name']
            patient_add.phone = request.POST['patient_phone']
            patient_add.patient_age = request.POST['patient_age']
            patient_add.address = request.POST['patient_address']
            patient_add.unique_id =  f'{unique_code(6)}'
            patient_add.save()

            patient_list = Patient.objects.all().order_by('-id')
            doctor_list = Doctor.objects.all().order_by('-id')
            report_list = Reportlist.objects.all().order_by('-id')
            data = {
            'doctor_list': doctor_list,
            'patient_list': patient_list,
            'report_list': report_list,
            }
            return render(request,  'report/add_lab_report.html', data)

        
        else:
            patient_id = request.POST['patient_name']
            doctor_id = request.POST['doctor_name']

            print('doctor_id', doctor_id)
           

            patient_add = Patient.objects.get(id=patient_id)
            referred_by_doctor_add = Doctor.objects.get(id=doctor_id)

            labCart = LabCart()
            
            labCart.patient = patient_add
            labCart.referred_by_doctor = referred_by_doctor_add
            labCart.save()
           
            report_name = request.POST.getlist('report_name')
            report_title_list = request.POST.getlist('report_title_list')
            report_commission_list = request.POST.getlist('report_commission_list')
            report_price_list = request.POST.getlist('report_price_list')

            # print(len(report_name))

            for report_title_list, report_commission_list,report_price_list,report_name in zip(report_title_list,report_commission_list,report_price_list, report_name):
                if len(report_name) == 0:
                    reportlistCart = ReportlistCart()
                    print('kkkkkkkkkk',report_title_list)
                    reportlistCart.title = report_title_list
                    reportlistCart.price = report_price_list
                    reportlistCart.commission = report_commission_list
                    reportlistCart.save()
                    print('no data')
                    # print('x',x)
                    # print('y',y)
                if len(report_name) > 0:
                    reportlistCart = ReportlistCart()
                    reportlistCart.title = report_title_list
                    reportlistCart.price = report_price_list
                    reportlistCart.commission = report_name
                    reportlistCart.save()



            # for report_id_list in report_id_list:
            #     print('report_id_list',report_id_list)


            # for report_name in report_name:

            #     print('bbbb',report_id_list)


            #     # print(len(report_name))
            #     if len(report_name) == 0:
            #         print('no data')
            #     if len(report_name) > 0:
            #         print('report_namereport_name',report_name)
                
                
            # print('vvvvvv',report_names)
            
            patient_list = Patient.objects.all().order_by('-id')
            doctor_list = Doctor.objects.all().order_by('-id')
            tests = ReportlistCart.objects.all().order_by('-id')
            data = {
            'doctor_list': doctor_list,
            'patient_list': patient_list,
            'tests': tests,
            }
            print('ffffffffff')
            return redirect('lab_cart')
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
                addDiagnosticAmount = CompanyIncome.objects.create(
                    amount=diagnosticProfit,
                    description=f'The revenue estimated was {diagnosticProfit} Taka.',
                    sources='The revenue generated from clinical laboratory services.',
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

                doctor = Doctor.objects.get(id=addProfit.doctor.id)
                total_amount = totalProfitAmount + doctor.total
                Doctor.objects.filter(id=addProfit.doctor.id).update(total=total_amount)


                return redirect('lab_report_list')
            else:
                return render(request,  'report/add_lab_report.html', {'form': LabForm()})
