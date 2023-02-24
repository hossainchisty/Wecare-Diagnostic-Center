# Basic Lib Import
from django.urls import path

from laboratory.views.add_lab_report_views import CreateLabView
from laboratory.views.add_lab_tests_views import CreateTestView
from laboratory.views.delete_lab_report_views import DeleteLabView
from laboratory.views.delete_tests_views import DeleteLabTestView
from laboratory.views.lab_report_list_views import LabReportListView
from laboratory.views.lab_tests_list_views import LabTestsListView
from laboratory.views.laboratory_pdf_views import LabReportPDF
from laboratory.views.update_lab_report_views import UpdateLabView
from laboratory.views.update_tests_views import UpdateTest

# Routing Implement
urlpatterns = [
    # Lab Report
    path('list', LabReportListView.as_view(), name='lab_report_list'),
    path('add', CreateLabView.as_view(), name='add_lab'),
    path('update/<int:pk>/', UpdateLabView.as_view(), name='update_lab'),
    path('delete/<int:pk>/', DeleteLabView, name='delete_lab'),

    # Tests
    path('tests', LabTestsListView.as_view(), name='lab_tests_list'),
    path('add/test/', CreateTestView.as_view(), name='add_lab_tests'),
    path('update/test/<int:pk>/', UpdateTest.as_view(), name='update_lab_test'),
    path('delete/test/<int:pk>/', DeleteLabTestView, name='delete_lab_test'),

    # PDF
    path('tests/<int:lab_id>/', LabReportPDF.as_view(), name='lab_report')
]
