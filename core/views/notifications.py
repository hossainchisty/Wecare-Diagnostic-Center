from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View


@method_decorator(login_required, name='dispatch')
class ExpiredMedicine(View):
    def get(self, request):
        return render(request, 'core/alerts/expired_medicine.html')


@method_decorator(login_required, name='dispatch')
class StockOutReport(View):
    def get(self, request):
        return render(request, 'core/alerts/stock_out.html')
