# Basic Lib Import

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View

from laboratory.models.lab_models import Lab


class LabReportListView(View):
    def get(self, request):
        ''' This will reutrn list of Lab '''
        lab_list = Lab.objects.all().order_by('-id')
        paginator = Paginator(lab_list, 10)
        page_number = request.GET.get('page')

        try:
            page_object = paginator.page(page_number)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_object = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_object = paginator.page(paginator.num_pages)

        context = {
            'lab': page_object,
        }
        return render(request, 'report/lab_report_list.html', context)
