# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from channels.handler import AsgiHandler
from channels import Group

# Create your views here.
def index(request):

    return render(request,'index.html')
