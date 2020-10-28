
from django.shortcuts import render
from .models import sender_information,goods_info,transform_info
from .tools.order.tools import set_order_number
# Create your views here.
def appstart_view(request):
    if request.method == 'GET':
        return render(request,'order/start.html',locals())
    elif request.method == 'POST':
        test1 = request.POST.get('test1')
        return render(request,'order/start.html',locals())

#收件人
def recipient_view(request):
    if request.method == 'GET':
        return render(request, 'order/recipient_view.html', locals())
    elif request.method == 'POST':
        # code
        name = request.POST.get('name')




        # code
        return render(request, 'order/recipient_view.html', locals())
#发件人
def sender_view(request):
    if request.method == 'GET':
        return render(request, 'order/sender_view.html', locals())
    elif request.method == 'POST':
        # code
        name = request.POST.get('name')
        # 补充


        sender_information.add_info(False,name=name)
        # code
        return render(request, 'order/sender_view.html', locals())

#地址簿
def address_page_view(request):
    if request.method == 'GET':
        return render(request, 'order/address_page_view.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/address_page_view.html', locals())

