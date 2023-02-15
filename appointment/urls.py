# Basic Lib Import
from django.urls import path

from appointment.views.add_appointment_views import CreateAppointmentView
from appointment.views.appointment_list_views import AppointmentListView
from appointment.views.cancelled_appointment_status import MakeAppointmentCancelView
from appointment.views.confirmed_appointment_status import MakeAppointmentConfirmedView
from appointment.views.delete_appointment_views import DeleteAppointment
from appointment.views.today_appointment_list_views import TodayAppointmentListView
from appointment.views.upcomming_appointment_list_views import UpcommingAppointmentListView
from appointment.views.update_appointment_views import UpdateAppointment

# Routing Implement
urlpatterns = [
    path('list', AppointmentListView.as_view(), name='appointment_list'),
    path('list/todays/', TodayAppointmentListView.as_view(), name='today_appointment_list'),
    path('list/upcomming/', UpcommingAppointmentListView.as_view(), name='upcomming_appointment_list'),
    path('add', CreateAppointmentView.as_view(), name='add_appointment'),
    path('update/<int:pk>/', UpdateAppointment.as_view(), name='update_appointment'),
    path('delete/<int:pk>/', DeleteAppointment.as_view(), name='delete_appointment'),

    # Status update
    path('cancle/<int:id>/', MakeAppointmentCancelView.as_view(), name='cancle_appointment'),
    path('confirmed/<int:id>/', MakeAppointmentConfirmedView.as_view(), name='confirmed_appointment'),

]
