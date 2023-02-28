# Basic Lib Import

from django.forms import ModelForm

from patient.models import Patient


class PaymentDueForm(ModelForm):
    ''' Payment due collections forms '''
    def __init__(self, *args, **kwargs):
        super(PaymentDueForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # self.fields['grand_total'].required = True
            # self.fields['paid_amount'].required = True
            self.fields['grand_total'].widget.attrs['disabled'] = 'disabled'
            self.fields['paid_amount'].widget.attrs['readonly'] = 'disabled'

    class Meta:
        model = Patient
        fields = ['grand_total', 'paid_amount', 'due']
