# Basic Lib Import
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .manager import UserManager


class User(AbstractUser):
    """ Customize default User model """
    USER_TYPE_CHOICES = (
      (1, 'doctor'),
      (2, 'patient'),
      (3, 'admin'),
      (4, 'subadmin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_number', ]
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(
        regex=r'^(?:\+88|88)?(01[3-9]\d{8})$')
    mobile_number = models.CharField(max_length=11, validators=[phone_regex], unique=True, help_text="Phone number must be entered in the format: '+8801XXXXXXXXX'.", null=True, blank=True) # noqa
    hospitial_logo = models.ImageField(upload_to='media/', null=True, blank=True)
    system_name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    hospitial_email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=40, null=True, blank=True)
    invoice_logo = models.ImageField(upload_to='media/', null=True, blank=True)
    contact_number = models.CharField(max_length=11, null=True, blank=True)
    footer_message = models.CharField(max_length=80, null=True, blank=True)
    is_verified = models.BooleanField(
        _('verified'),
        default=False,
        help_text=_(
            'Designates whether this user has been verified. '
            'Un-verified users cannot log in.'
        ),
    )
    is_doctor = models.BooleanField(
        _('doctor'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as doctor.'
        ),
    )
    is_patient = models.BooleanField(
        _('patient'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as patient.'
        ),
    )
    is_admin = models.BooleanField(
        _('admin'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as admin.'
        ),
    )
    is_subadmin = models.BooleanField(
        _('subadmin'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as subadmin.'
        ),
    )
    is_hr = models.BooleanField(
        _('hr'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as Human resources (HR).'
        ),
    )
    is_accountant = models.BooleanField(
        _('accountant'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as accountant.'
        ),
    )
    is_employee = models.BooleanField(
        _('employee'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as employee.'
        ),
    )
    is_nurse = models.BooleanField(
        _('nurse'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as nurse.'
        ),
    )
    is_pharmascist = models.BooleanField(
        _('pharmascist'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as pharmascist.'
        ),
    )
    is_laboratoriest = models.BooleanField(
        _('laboratoriest'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as laboratoriest.'
        ),
    )
    is_receptionist = models.BooleanField(
        _('receptionist'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as receptionist.'
        ),
    )
    otp = models.SmallIntegerField(
        help_text='One Time Password',
        null=True, blank=True
    )
    token = models.CharField(
        verbose_name=_('Token'),
        max_length=100,
        unique=True,
        null=True, blank=True, editable=False,
        help_text='Token for authentication'
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP Address'),
        help_text='IP Address',
        blank=True, null=True
    )
    password_changes_datatime = models.DateTimeField(
        verbose_name=_('Password changes datatime'),
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(default=now, editable=False)

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
