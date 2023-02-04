
from django.shortcuts import redirect, render
from django.views import View

from department.models import Department


class CreateDepartment(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'department/add_department.html')

    def post(self, request, *args, **kwargs):
        ''' Create a new department '''
        department_name = request.POST.get('department_name')
        description = request.POST.get('description')
        department = Department(department_name=department_name, description=description)
        department.save()
        """Provide a redirect on GET request."""
        return redirect('department_list')
