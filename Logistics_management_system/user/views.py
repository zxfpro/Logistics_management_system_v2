from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
def appstart_view(request):
    if request.method == 'GET':
        return render(request,'user/start.html',locals())
    elif request.method == 'POST':

        return render(request,'user/start.html',locals())


def login(request):
    if request.method == 'GET':
        return render(request,'user/login.html',locals())
    elif request.method == 'POST':

        return render(request,'user/login.html',locals())


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html', locals())
    elif request.method == 'POST':

        return render(request, 'user/register.html', locals())

def check_user(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        user = request.POST.get('user'),
        print('user>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',user)
        if user[0] =='11':
            return HttpResponseRedirect('/order/appstart')#用户登录
        elif user[0] =='00':
            return HttpResponseRedirect('/order/express_main')#快递员登录
        elif user[0] =='01':
            return HttpResponseRedirect('/waybill/wayBill_main')#物流人员登录
        elif user[0] =='10':
            return HttpResponseRedirect('/transfer_station/transform_view')#中转站登录
        else:
            return HttpResponse('error')

