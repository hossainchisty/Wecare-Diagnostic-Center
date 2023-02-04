# Basic Lib Import
from django.urls import path

from department.views.add_department_views import CreateDepartment
from department.views.delete_department_views import DeleteDepartment
from department.views.department_list_views import DepartmentListView
from department.views.update_department_views import UpdateDepartment

# Routing Implement
urlpatterns = [
    path('list', DepartmentListView.as_view(), name='department_list'),
    path('add', CreateDepartment.as_view(), name='add_department'),
    path('update/<int:pk>/', UpdateDepartment.as_view(), name='update_department'),
    path('delete/<pk>', DeleteDepartment.as_view(), name='delete_department'),
]
