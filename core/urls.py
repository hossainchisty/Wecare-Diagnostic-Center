# Basic Lib Import
from django.urls import path

from core.views.core_views import Dashboard
from core.views.notifications import ExpiredMedicine, StockOutReport

# Routing Implement
urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('notifications/expired/medicine/', ExpiredMedicine.as_view(), name='expired_medicine'),
    path('notifications/stock/out/medicine/', StockOutReport.as_view(), name='stock_out_medicine'),
]
