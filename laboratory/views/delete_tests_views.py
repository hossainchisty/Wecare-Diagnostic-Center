# Basic Lib Import
from django.shortcuts import redirect

from laboratory.models import Reportlist


def DeleteLabTestView(request, pk):
    if request.method == "POST":
        tests = Reportlist.objects.get(id=pk)
        tests.delete()
        return redirect('lab_tests_list')
