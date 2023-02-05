# Basic Lib Import
from django import template

from patient.models import Patient

register = template.Library()


@register.simple_tag
def total_patient():
    ''' This method is used to get total patient. '''
    return Patient.objects.all().count()
