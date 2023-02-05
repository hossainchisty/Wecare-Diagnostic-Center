# Basic Lib Import

from datetime import datetime, timedelta

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View

from appointment.models import Appointment


class UpcommingAppointmentListView(View):
    def get(self, request):
        ''' This will reutrn list of upcomming appointments '''
        # Get today's date from last 7 days
        upcomming_appointments = Appointment.objects.filter(date__gte=datetime.now()-timedelta(days=7))
        paginator = Paginator(upcomming_appointments, 10)
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
        return render(request, 'appointment/upcomming_appointment_list.html', context)
