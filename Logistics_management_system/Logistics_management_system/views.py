
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def start(request):
    if request.method =='GET':

        return HttpResponseRedirect('/user/login')

    if request.method =='POST':

        return HttpResponseRedirect('/user/login')

    
