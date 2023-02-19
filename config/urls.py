# flake8: noqa

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'Diagnostic Center Portal'
admin.site.site_title = 'Diagnostic Center Management'
admin.site.index_title = 'Diagnostic Center Management'
admin.autodiscover()

urlpatterns = [
    path('', include('core.urls')),
    path('department/', include('department.urls')),
    path('doctor/', include('doctor.urls')),
    path('schedule/', include('schedule.urls')),
    path('patient/', include('patient.urls')),
    path('appointment/', include('appointment.urls')),
    path('lab/report/', include('laboratory.urls')),
    path('expense/', include('expense.urls')),
    path('report/', include('report.urls')),
    path('auth/', include('authenticator.urls')),
    path('front/', include('frontapp.urls')),

    # Admin Stuff
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
