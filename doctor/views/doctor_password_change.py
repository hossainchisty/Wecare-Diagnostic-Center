from django.shortcuts import render
from django.views.generic import View

from doctor.models.doctor_model import Doctor


class ChangePassword(View):
    def get(self, request, doctor_id):
        ''' This will change doctor password '''
        '''
        TODO: 1. check old password if its current then allow user to change password with new onece
        '''

        old_password = request.GET.get('old_password')
        print(old_password)
        docId = Doctor.objects.get(id=doctor_id).filter(password=old_password)
        print(docId)
        return render(request, 'doctor/change_password.html')

    # def post(self, request, *args, **kwargs):
    #     ''' Create a new Doctor '''
    #     if request.method == 'POST':
    #         old_password = request.POST.get('old_password')
    #         check = Doctor.objects.get(password__exact=old_password)
    #         print(check)
    #     else:
    #         return render(request, 'doctor/change_password.html')
