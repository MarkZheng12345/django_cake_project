from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .forms import RegistrationForm
# Create your views here.


def registration(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('/')
    else:
        reg_form = RegistrationForm()
    return render(request, 'registration.html', {'reg_form': reg_form})



def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                print('email already registered............................')
                messages.info(request, 'email already exists')
                return redirect('register')
            else:
                oUser = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                oUser.save()
                print('success.......................')
                return redirect('login')
        else:
            print('password do not match..........................')
            messages.info(request, 'passwords do not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')