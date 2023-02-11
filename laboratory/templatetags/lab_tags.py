# Basic Lib Import
from django import template

from laboratory.models import Lab

register = template.Library()


@register.simple_tag
def total_lab_report():
    ''' This method is used to get total lab report. '''
    return Lab.objects.all().count()
