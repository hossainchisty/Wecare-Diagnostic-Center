# Basic Lib Import

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View

from laboratory.models import Reportlist


class LabTestsListView(View):
    def get(self, request):
        ''' This will reutrn list of Lab tests '''
        tests_list = Reportlist.objects.all().order_by('-id')
        paginator = Paginator(tests_list, 10)
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
            'tests': page_object,
        }
        return render(request, 'report/lab_tests_list.html', context)
