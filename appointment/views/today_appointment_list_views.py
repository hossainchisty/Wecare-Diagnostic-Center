# Basic Lib Import

from datetime import date

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View

from appointment.models import Appointment


class TodayAppointmentListView(View):
    def get(self, request):
        ''' This will reutrn list of today appointment '''
        today = date.today()
        today_list = Appointment.objects.filter(created_at__contains=today)
        paginator = Paginator(today_list, 10)
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
            'appointment': page_object,
        }
        return render(request, 'appointment/today_appointment_list.html', context)
