# Basic Lib Import
from django.urls import path

from laboratory.views.add_lab_report_views import CreateLabView
from laboratory.views.delete_lab_report_views import DeleteLabView
from laboratory.views.lab_report_list_views import LabReportListView
from laboratory.views.update_lab_report_views import UpdateLabView

# Routing Implement
urlpatterns = [
    path('list', LabReportListView.as_view(), name='lab_report_list'),
    path('add', CreateLabView.as_view(), name='add_lab'),
    path('update/<int:pk>/', UpdateLabView.as_view(), name='update_lab'),
    path('delete/<int:pk>/', DeleteLabView.as_view(), name='delete_lab'),
]
