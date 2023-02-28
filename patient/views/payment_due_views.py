# Basic Lib Import
# from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from patient.forms.payment_due_form import PaymentDueForm
from patient.models import Patient


class DuePayment(UpdateView):
    model = Patient
    form_class = PaymentDueForm
    template_name = 'patient/payment_due_form.html'
    success_url = reverse_lazy('patient_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        # if obj.user != self.request.user:
        #     raise PermissionDenied("You are not allowed to edit this customer.")
        return obj
