from django.contrib import admin

from .models import Doctor, DoctorVisit

admin.site.register(Doctor)
admin.site.register(DoctorVisit)
