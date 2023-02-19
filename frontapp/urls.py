from django.urls import path
from frontapp.views import *

from frontapp.views import load_cities

# Routing Implement
urlpatterns = [
    path('', Index.as_view(), name='index_view'),
    path('about', About.as_view(), name='about_view'),
    path('contact', Contact.as_view(), name='contact_view'),
    path('price', Price.as_view(), name='price_view'),
    path('service', Service.as_view(), name='service_view'),
    path('team', Team.as_view(), name='team_view'),
    path('testimonial', Testimonial.as_view(), name='testimonial_view'),
    path('appointment', Appointment.as_view(), name='appointment_view'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]
