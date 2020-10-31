from django.http import HttpResponse,HttpResponseRedirect
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
        responds = HttpResponse('缓存')
        responds.set_cookie('re_name',request.POST.get('re_name'),100)


        return render(request, 'order/main_order_web.html', locals())

#发件人
def sender_view(request):
    if request.method == 'GET':
        return render(request, 'order/sender_view.html', locals())
    elif request.method == 'POST':
        print('寄件人提交成功')
        responds = HttpResponse('提交')
        name = request.POST.get('name')
        responds.set_cookie('name',name,10000)
        print('kook设置成功',request.COOKIES.get('name'))

        return HttpResponseRedirect('/order/main_order_web')
        # return render(request, 'order/main_order_web.html', locals())
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
    print('进入main界面')


    if request.method == 'GET':
        print('进入main get界面')
        name = request.COOKIES.get('name')

        re_name = request.COOKIES.get('re_name')
        print('name=', name)
        print('rename=', re_name)
        return render(request, 'order/main_order_web.html', locals())
    elif request.method == 'POST':
        print('进入main post界面')
        # name = request.POST.get('name')
        # re_name = request.POST.get('re_name')
        name = request.COOKIES.get('name')
        re_name = request.COOKIES.get('re_name')
        print('name=',name)
        print('rename=',re_name)

        # code
        # responds = HttpResponse('缓存')
        # responds.set_cookie('name',request.POST.get('name'),100)
        # responds.set_cookie('re_name',request.POST.get('re_name'),100)
        #
        # name = request.COOKIES.get('name','2')
        # re_name = request.COOKIES.get('re_name')
        # name = request.POST.get('name')
        # re_name = request.POST.get('re_name')
        # city = request.POST.get('city')
        # re_city = request.POST.get('re_city')
        # telephone = request.POST.get('telephone')
        # re_telephone = request.POST.get('re_telephone')
        # detailed_address = request.POST.get('detailed_address')
        # re_detailed_address = request.POST.get('re_detailed_address')
        # name_of_company = request.POST.get('name_of_company')
        # re_name_of_company = request.POST.get('re_name_of_company')
        #
        #
        # code
        return render(request, 'order/main_order_web.html', locals())

def create_order(request):
    pass



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


def text(request):
    if request.method == 'GET':
        return render(request, 'order/text.html', locals())
    elif request.method == 'POST':
        # code

        # code
        return render(request, 'order/text.html', locals())
