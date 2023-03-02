from authenticator.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def SignInView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'Login Successfull')
            # return redirect('dashboard')
            if user.is_sub:
                return redirect('dashboard')
            elif user.is_doctor:
                return redirect('doctordashboard')
            elif user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('dashboard')
            url = request.META.get('HTTP_REFERER')
        else:
            # messages.error(request, 'Invalid login crisidals')
            return redirect('sign-in')
    return render(request, 'authenticator/login.html')
