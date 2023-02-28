from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import View

from appointment.models import Appointment
from django.http import JsonResponse, HttpResponseBadRequest


@method_decorator(login_required, name='dispatch')
class AppointmentNotify(View):
    def get(self, request):
        ''' This will reutrn list of appointment '''
        appointment_list = Appointment.objects.filter(is_read=False)
        unread_notifications = Appointment.objects.filter(user=request.user, is_read=False).count()
        paginator = Paginator(appointment_list, 10)
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
            'unread_notifications': unread_notifications
        }
        return render(request, 'appointment/appointment_notification.html', context)


def UnreadNotify(request):
    ''' This will reutrn list of appointment '''
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            unread_notifications = Appointment.objects.filter(is_read=False).count()
            print(unread_notifications)
            return JsonResponse({'unread_notifications': unread_notifications})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
