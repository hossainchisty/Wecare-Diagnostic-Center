# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from schedule.forms.holidays_form import HolidaysForm
from schedule.models import Holiday


class UpdateHoliday(UpdateView):
    model = Holiday
    fields = ['doctor', 'date']
    # FIXME: Date pickup not showing here
    from_class = HolidaysForm
    template_name = 'schedule/holiday_form.html'
    success_url = reverse_lazy('holidays_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this customer.")
        return obj
