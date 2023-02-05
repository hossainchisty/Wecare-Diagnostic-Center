# Basic Lib Import
from django import template

from doctor.models import Doctor

register = template.Library()


@register.simple_tag
def total_doctor():
    ''' This method is used to get total doctor. '''
    return Doctor.objects.all().count()
