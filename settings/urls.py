# Basic Lib Import
from django.urls import path

from settings.views.password_change_views import passwordChangeView
from settings.views.privacy_and_security_views import PrivacyAndSecurityView
from settings.views.settings_views import settings

# Routing Implement
urlpatterns = [
    path('', settings, name='settings'),
    path('password/change/', passwordChangeView, name='password_change'),
    path('accounts/privacy_and_security/', PrivacyAndSecurityView.as_view(), name='privacy_and_security')
]
