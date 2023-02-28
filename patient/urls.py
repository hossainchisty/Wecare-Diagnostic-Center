# Basic Lib Import
from django.urls import path

from patient.views.add_patient_views import CreatePatientView
from patient.views.delete_patient_views import DeletePatient
from patient.views.patient_list_views import PatientListView
from patient.views.update_patient_views import UpdatePatient
from patient.views.patient_details_views import PatientDetailsView
from patient.views.due_collection_views import DueCollection, CollectDueAmount
from patient.views.payment_due_views import DuePayment

# Routing Implement
urlpatterns = [
    path('list', PatientListView.as_view(), name='patient_list'),
    path('add', CreatePatientView.as_view(), name='add_patient'),
    path('update/<int:pk>/', UpdatePatient.as_view(), name='update_patient'),
    path('delete/<int:pk>/', DeletePatient, name='delete_patient'),
    path('details/<str:id>/<str:uhid>/', PatientDetailsView, name='patient_details'),
    path('due/collection/', DueCollection.as_view(), name='patient_due'),
    path('collect/due/amount/<str:id>/<str:uhid>/', CollectDueAmount.as_view(), name='collect_due_amount'),
    path('edit/due/amount/<str:pk>/<str:uhid>/', DuePayment.as_view(), name='due_payment'),
]
