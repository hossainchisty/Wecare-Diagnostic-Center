from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from laboratory.models import Lab, Reportlist


@admin.register(Reportlist)
class ReportlistAdmin(ImportExportModelAdmin):
    list_display = ('title', 'price')


@admin.register(Lab)
class LabAdmin(ImportExportModelAdmin):
    list_display = ('patient', 'referred_by_doctor', 'total', 'report_status')
