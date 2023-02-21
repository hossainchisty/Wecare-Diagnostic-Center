# flake8: noqa
# Basic Lib Import

from django.contrib.auth import views as auth_views
from django.urls import path

from authenticator.views.login_views import SignInView
from authenticator.views.logout_views import SignOutView
from authenticator.views.doctor_login_views import DoctorSignInView

# Routing Implement
urlpatterns = [
    path('portal/sign-in/', SignInView, name='sign-in'),
    path('doctor/portal/sign-in/', DoctorSignInView, name='doctor-sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
]
