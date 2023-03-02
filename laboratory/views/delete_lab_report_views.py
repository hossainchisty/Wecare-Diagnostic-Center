
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from laboratory.models.lab_models import *
from django.shortcuts import redirect, render


class DeleteLabView(DeleteView):
    model = Lab
    success_url = reverse_lazy('lab_report_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to delete this customer.")
        return obj
    
class DeleteReportCart(DeleteView):
    model = ReportlistCart
    success_url = reverse_lazy('lab_cart')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to delete this customer.")
        return obj



# def labCart(request):


#     return redirect('lab_cart')


def deletereportcart(request, id):
    delete = ReportlistCart.objects.get(id=id)
    delete.is_delete = True
    delete.save()
    return redirect('lab_cart')


