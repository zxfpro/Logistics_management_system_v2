
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def start(request):
    if request.method =='GET':

        return render(request,'start.html',locals())
    if request.method =='POST':
        text = request.POST.get('text')

        return render(request,'start.html',locals())
    
    
