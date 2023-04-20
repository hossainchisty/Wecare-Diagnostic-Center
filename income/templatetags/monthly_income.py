from django import template
from django.db.models import Sum
from income.models import CompanyIncome
from django.db.models.functions import TruncMonth
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.simple_tag
def get_monthly_income(default=0.00):
    ''' Calculate the total monthly income '''
    return intcomma(CompanyIncome.objects.annotate(month=TruncMonth('created_at')).values('month').aggregate(Sum('amount'))['amount__sum']) or default # noqa