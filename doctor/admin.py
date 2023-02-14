from django.contrib import admin

from .models import Doctor, DoctorProfit, DoctorVisit

admin.site.register(DoctorProfit)
admin.site.register(DoctorVisit)
admin.site.register(Doctor)
