# Basic Lib Import
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View

from laboratory.models import Lab
from utility.render_to_pdf import generate_pdf


class DownloadLabPDF(LoginRequiredMixin, View):
    ''' Automaticly downloads to PDF file. '''
    def get(self, request, lab_id):
        Labreport = Lab.objects.get(id=lab_id)
        pdf = generate_pdf('laboratory/report/pdf/lab_report.html', {'lab': Labreport})
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Lab-Tests-Data-%s.pdf" % date.today()
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response
