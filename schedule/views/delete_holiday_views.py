# Basic Lib Import

# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from schedule.models import Holiday


class DeleteHoliday(DeleteView):
    model = Holiday
    success_url = reverse_lazy('holidays_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to delete this customer.")
        return obj
