# Basic Lib Import
from django.urls import path

from patient.views.add_patient_views import CreatePatientView
from patient.views.delete_patient_views import DeletePatient
from patient.views.patient_list_views import PatientListView
from patient.views.update_patient_views import UpdatePatient

# Routing Implement
urlpatterns = [
    path('list', PatientListView.as_view(), name='patient_list'),
    path('add', CreatePatientView.as_view(), name='add_patient'),
    path('update/<int:pk>/', UpdatePatient.as_view(), name='update_patient'),
    path('delete/<int:pk>/', DeletePatient.as_view(), name='delete_patient'),
]