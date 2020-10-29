
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

        name = request.POST.get('name')
        telephone = request.POST.get('telephone')
        city = request.POST.get('city')
        detailed_address = request.POST.get('detailed_address')
        name_of_company = request.POST.get('name_of_company')

        sender_information.add_info(True, name=name, telephone=telephone, city=city, detailed_address=detailed_address,
                                    name_of_company=name_of_company,order_number='wait')

        return render(request, 'order/recipient_view.html', locals())
#发件人
def sender_view(request):
    if request.method == 'GET':
        return render(request, 'order/sender_view.html', locals())
    elif request.method == 'POST':

        name = request.POST.get('name')
        telephone = request.POST.get('telephone')
        city = request.POST.get('city')
        detailed_address = request.POST.get('detailed_address')
        name_of_company = request.POST.get('name_of_company')


        #发件人是False 收件人是True
        sender_information.add_info(False,name=name,telephone=telephone,city=city,
                                    detailed_address=detailed_address,
                                    name_of_company=name_of_company,order_number='wait')
        return render(request, 'order/sender_view.html', locals())

#地址簿
def address_page_view(request):
    if request.method == 'GET':
        return render(request, 'order/address_page_view.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/address_page_view.html', locals())

def address_write_by_page(request):
    if request.method == 'GET':
        return render(request, 'order/address_write_by_page.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/address_write_by_page.html', locals())



#主订单模块
def main_order_web(request):
    if request.method == 'GET':
        return render(request, 'order/main_order_web.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/main_order_web.html', locals())


#查询订单页面
def main_search_web(request):
    if request.method == 'GET':
        return render(request, 'order/main_search_web.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/main_search_web.html', locals())

#我的
def main_my_info(request):
    if request.method == 'GET':
        return render(request, 'order/main_my_info.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/main_my_info.html', locals())

#快递小哥
def express_main(request):
    if request.method == 'GET':
        return render(request, 'order/express_main.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/express_main.html', locals())


def express_write_goods_info(request):
    if request.method == 'GET':
        return render(request, 'order/express_write_goods_info.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/express_write_goods_info.html', locals())


#订单打印页面
def express_order_print(request):
    if request.method == 'GET':
        return render(request, 'order/express_order_print.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/express_order_print.html', locals())

