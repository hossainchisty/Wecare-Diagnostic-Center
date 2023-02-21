# Basic Lib Import
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """ Abstract base classe some common information """
    user = models.OneToOneField('authenticator.User', verbose_name=_('User'), on_delete=models.CASCADE, null=True, blank=True) # noqa
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        ordering = ['-created_at']
        abstract = True
