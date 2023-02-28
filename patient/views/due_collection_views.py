# Basic Lib Import
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from patient.models import Patient


class DueCollection(View):
    ''' Due Collection '''

    def get(self, request):
        ''' Respond to a GET request '''
        due_list = Patient.objects.filter(payment_status='due')
        due_amount = due_list.aggregate(Sum('due'))['due__sum']
        print(due_amount)

        paginator = Paginator(due_list, 10)
        page_number = request.GET.get('page')

        try:
            page_object = paginator.page(page_number)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_object = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_object = paginator.page(paginator.num_pages)

        context = {
            'due_list': page_object,
            'due_amount': due_amount,
        }
        return render(request, 'patient/patient_due_collection.html', context)


class CollectDueAmount(View):
    ''' Due Collection '''

    def get(self, request,  id, uhid):
        ''' Respond to a GET request '''
        patient_bills = get_object_or_404(Patient, unique_id=uhid)
        context = {
            'data': patient_bills
        }
        return render(request, 'patient/collection_due_payment.html', context)
