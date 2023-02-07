# Basic Lib Import
from django.urls import path

from report.views.lab_report_list_views import LabReportListView

# Routing Implement
urlpatterns = [
    path('list', LabReportListView.as_view(), name='lab_report_list'),
    # path('add', CreatePatientView.as_view(), name='add_patient'),
    # path('update/<int:pk>/', UpdatePatient.as_view(), name='update_patient'),
    # path('delete/<int:pk>/', DeletePatient.as_view(), name='delete_patient'),
]
