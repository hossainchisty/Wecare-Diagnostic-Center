# Basic Lib Import
from django.urls import path

from schedule.views.add_holidays_views import CreateHolidays
from schedule.views.add_schedule_views import CreateSchedule
from schedule.views.delete_holiday_views import DeleteHoliday
from schedule.views.delete_schedule_views import DeleteSchedule
from schedule.views.holidays_list_views import HolidaysListView
from schedule.views.schedule_list_views import ScheduleListView
from schedule.views.update_holiday_views import UpdateHoliday

# Routing Implement
urlpatterns = [
    path('list', ScheduleListView.as_view(), name='schedule_list'),
    path('add', CreateSchedule.as_view(), name='add_schedule'),
    path('delete/<pk>', DeleteSchedule.as_view(), name='delete_schedule'),
    path('delete/holiday/<pk>', DeleteHoliday.as_view(), name='delete_holiday'),

    path('holidays', HolidaysListView.as_view(), name='holidays_list'),
    path('add/holiday', CreateHolidays.as_view(), name='add_holiday'),
    path('update/<int:pk>/', UpdateHoliday.as_view(), name='update_holiday'),
]
