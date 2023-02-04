# Basic Lib Import

# from datetime import datetime

from django.shortcuts import redirect, render
from django.views.generic import View

from schedule.forms.schedule_form import ScheduleForm


class CreateSchedule(View):
    def get(self, request, *args, **kwargs):
        return render(request,  'schedule/add_schedule.html', {'form': ScheduleForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Schedule '''
        form = ScheduleForm(request.POST)
        # Automatically set to the currently logged-in user
        # form.instance.user = request.user
        if form.is_valid():
            # form.instance.recently_added = datetime.now()
            form.save()
            """Provide a redirect on GET request."""
            return redirect('schedule_list')
        else:
            return render(request,  'schedule/add_schedule.html', {'form': ScheduleForm()})
