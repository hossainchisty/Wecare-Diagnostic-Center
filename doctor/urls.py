# Basic Lib Import
from django.urls import path

from doctor.views.add_doctor_views import CreateDoctorView
from doctor.views.add_doctor_visit_charge_views import CreateDoctorVisitView
from doctor.views.delete_doctor_views import DeleteDoctor
from doctor.views.delete_doctor_visit_views import DeleteDoctorVisit
from doctor.views.doctor_list_views import DoctorListView
from doctor.views.doctor_visit_list import DoctorVisitListView
from doctor.views.holiday_history_views import DoctorholidayListView
from doctor.views.update_doctor_views import UpdateDoctor
from doctor.views.update_doctor_visit_views import UpdateDoctorVisit
from doctor.views.doctor_details_views import DoctorDetailsView
from doctor.views.doctor_password_change import ChangePassword


# Routing Implement
urlpatterns = [
    path('list', DoctorListView.as_view(), name='doctor_list'),
    path('add', CreateDoctorView.as_view(), name='add_doctor'),
    path('add/visit/charges', CreateDoctorVisitView.as_view(), name='add_doctor_visit'),
    path('update/<int:pk>/', UpdateDoctor.as_view(), name='update_doctor'),
    path('update/visit/<int:pk>/', UpdateDoctorVisit.as_view(), name='update_doctor_visit'),
    path('schedule/holidays/<int:doctor_id>/', DoctorholidayListView.as_view(), name='doctor_holiday_list'),
    path('delete/<int:pk>', DeleteDoctor, name='delete_doctor'),
    path('visit/list', DoctorVisitListView.as_view(), name='doctor_visit_list'),
    path('delete/visit/<int:pk>', DeleteDoctorVisit.as_view(), name='delete_doctor_visit'),


    path('details/<int:detail_id>', DoctorDetailsView, name='doctor_details'),
    path('change/password/<str:doctor_id>', ChangePassword.as_view(), name='change_doctor_password')
]
