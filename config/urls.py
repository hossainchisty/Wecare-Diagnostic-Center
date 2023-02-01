# flake8: noqa

from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'Diagnostic Center Portal'
admin.site.site_title = 'Diagnostic Center Management'
admin.site.index_title = 'Diagnostic Center Management'
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]
