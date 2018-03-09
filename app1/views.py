from django.shortcuts import render
from pip._vendor import requests

from app1.forms import ClientForms, UserForms, UserProfileInfoForm
from app1.modelforms import NewClientForm
from app1.models import Clients, User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from urllib import request



# Create your views here.
def index_main(request):
    if request.method == 'POST':
        form = ClientForms(request.POST)
        if form.is_valid():
            first_name = form.clean()["first_name"]
            last_name = form.clean()["last_name"]
            email = form.clean()["email"]
            Clients.objects.get_or_create(FIRST_NAME=first_name, LAST_NAME=last_name, E_MAIL=email)
    return render(request, 'app1/main.html', {"form": ClientForms})

@login_required
def special(request):
    return render(request, 'app1/special.html',  {"user": User})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def clients(request):
    client_arr = Clients.objects.all()
    my_dict = {"data": client_arr}
    return render(request, 'app1/client.html', my_dict)

def users(request):
    form = NewClientForm()
    if request.method == 'POST':
        form = NewClientForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return clients(request)
        else:
            print("ERROR: FORM INVALID")
        
    return render(request, 'app1/main.html', {"form":form})

def index(request):
    return render(request, 'app1/index.html')

def other(request):
    return render(request, 'app1/other.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForms(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        else:
            print(user_form.errors, profile_form.errors)

    return render(request, 'app1/registration.html', {"forms": UserForms, "profile_form": UserProfileInfoForm,"registered":registered})

def user_login(request):
     if request.method == 'POST':
         username=request.POST.get("username")
         password=request.POST.get("password")
         
         user = authenticate(username=username, password=password)
         
         if user:
             if user.is_active:
                 login(request, user=user)
                 return HttpResponseRedirect(reverse('index'))
             else:
                 return HttpResponse("Account not active")
         else:
             print("Login failed")
             print("username: {}, password: {}".format(username, password))
             return HttpResponse("invalid login details supplied")
     else:
        return render(request, 'app1/login.html')