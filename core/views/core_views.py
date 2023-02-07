from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View


@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    def get(self, request):
        ''''
        Main dashboard view for the application.
        '''
        return render(request, 'core/dashboard.html')
