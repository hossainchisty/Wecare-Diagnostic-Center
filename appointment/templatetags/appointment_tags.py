# Basic Lib Import
from django import template

from appointment.models import Appointment

register = template.Library()


@register.simple_tag
def total_appointment():
    ''' This method is used to get total appointment. '''
    return Appointment.objects.all().count()


@register.simple_tag
def c():
    ''' This method is used to get total appointment. '''
    return Appointment.objects.filter(is_read=False).count()
