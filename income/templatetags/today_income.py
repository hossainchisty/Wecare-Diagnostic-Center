from datetime import date

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Sum
from income.models import CompanyIncome

register = template.Library()


@register.simple_tag
def get_today_income(default=0.00):
    ''' Calculate the today income . '''
    return intcomma(CompanyIncome.objects.filter(created_at=date.today()).aggregate(Sum('amount'))['amount__sum'] or default) # noqa
