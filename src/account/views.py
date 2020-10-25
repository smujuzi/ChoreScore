
from .models import *

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm

from django.views import View


def register(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    if request.POST:
       form = RegistrationForm(request.POST)

       if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            context = {}
            return render(request, 'account/login.html', context)


       else:
          context['registration_form'] = form
    else: 
        form = RegistrationForm()
        context['registration_form'] = form
        return render(request, 'account/register.html', context)


def login_view(request):

    context = {}
    print("In Login")
    user = request.user
    if user.is_authenticated:
        return render(request, 'account/home.html', context)

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
         email = request.POST['email']
         password = request.POST['password']
         user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect("list")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form


    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_view')

def home_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'account/home.html', context)