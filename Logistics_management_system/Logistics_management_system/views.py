
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def start(request):
    if request.method =='GET':

        return HttpResponseRedirect('/user/appstart')

    if request.method =='POST':
        text = request.POST.get('text')

        return HttpResponseRedirect('/user/appstart')

    
