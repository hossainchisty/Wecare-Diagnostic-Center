# Basic Lib Import

from django.shortcuts import redirect, render
from django.views.generic import View

from schedule.forms.holidays_form import HolidaysForm


class CreateHolidays(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'schedule/add_holidays.html', {'form': HolidaysForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new holidays '''
        form = HolidaysForm(request.POST)
        # Automatically set to the currently logged-in user
        # form.instance.user = request.user
        if form.is_valid():
            form.save()
            """Provide a redirect on GET request."""
            return redirect('holidays_list')
        else:
            return render(request,  'schedule/add_holidays.html', {'form': HolidaysForm()})
