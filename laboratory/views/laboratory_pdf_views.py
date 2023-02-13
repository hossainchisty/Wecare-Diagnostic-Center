# Basic Lib Import
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View

from laboratory.models import Lab
from utility.render_to_pdf import generate_pdf


class LabReportPDF(LoginRequiredMixin, View):
    ''' This view will show lab tests pdf '''
    def get(self, request, lab_id):
        Labreport = Lab.objects.get(id=lab_id)
        tests = Labreport.report_name.all()
        pdf = generate_pdf('report/pdf/lab_report.html', {'lab': Labreport, 'tests': tests})
        return HttpResponse(pdf, content_type='application/pdf')
