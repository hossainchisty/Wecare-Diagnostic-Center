from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def SignInView(request):
    ''' Sign in views '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user is None:
            messages.info(request, '%s Not found!' % username)
            return redirect('sign-in')
        auth_user = authenticate(username=username, password=password)
        if auth_user is None:
            messages.info(request, 'Wrong credentials')
            return redirect('sign-in')
        login(request, auth_user)
        return redirect('dashboard')
    return render(request, 'authenticator/login.html')
