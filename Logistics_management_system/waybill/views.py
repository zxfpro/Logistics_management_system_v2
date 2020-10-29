
from django.shortcuts import render
from .tools.waybill.tools import *
# Create your views here.
def appstart_view(request):
    if request.method == 'GET':
        return render(request,'waybill/start.html',locals())
    elif request.method == 'POST':
        test1 = request.POST.get('test1')
        return render(request,'waybill/start.html',locals())

def wayBill_main(request):
    if request.method == 'GET':
        return render(request,'waybill/wayBill_main.html',locals())
    elif request.method == 'POST':

        return render(request,'waybill/wayBill_main.html',locals())
