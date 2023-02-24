# Basic Lib Import

from django.shortcuts import redirect
from laboratory.models import Lab


def DeleteLabView(request, pk):
    if request.method == "POST":
        labs = Lab.objects.get(id=pk)
        labs.delete()
        return redirect('lab_report_list')
