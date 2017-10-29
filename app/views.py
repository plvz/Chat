# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
@login_required
def index(request):
    current_user = request.user
    print(current_user.username)
    users = User.objects.all()
    return render(request,'index.html',{'users' : users, 'current_user' : current_user.username})

def signup(request):
    form = UserForm()
    return render(request,'sign-up.html',{'form' : form})

def post_user(request):
    form = UserForm(request.POST, request.FILES)
    if form.is_valid():
        user = User.objects.create_user(request.POST['username'], 'lennon@thebeatles.com', request.POST['password'])
        user.save()
    return HttpResponseRedirect('/')

def signin(request):
    form = UserForm()
    return render(request,'sign-in.html',{'form' : form})

def authentication(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    print(username +"  :  "+password)
    print(user)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        print('succes authentication')
        return HttpResponseRedirect('/',{'user' : user})

    else:
        # Return an 'invalid login' error message.
        print('error authentication')
        return HttpResponseRedirect('/')
