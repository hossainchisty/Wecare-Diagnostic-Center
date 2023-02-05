# Basic Lib Import
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View

from schedule.models import Holiday


class DoctorholidayListView(View):
    def get(self, request, doctor_id):
        ''' This will reutrn history of holiday '''
        holiday_history_list = Holiday.objects.filter(doctor=doctor_id)
        paginator = Paginator(holiday_history_list, 10)
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
            'holiday': page_object,
        }
        return render(request, 'doctor/doctor_holidays.html', context)
