# Basic Lib Import
from django.urls import path

from core.views.core_views import Dashboard

# Routing Implement
urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]
