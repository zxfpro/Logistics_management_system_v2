
from django.urls import path
from . import views

urlpatterns = [

    path('appstart',views.appstart_view),
    path('recipient',views.recipient_view),
    path('sender',views.sender_view),
    path('address_page',views.address_page_view),
    path('address_write_by_page',views.address_write_by_page),
    path('main_order_web',views.main_order_web),
    path('main_search_web',views.main_search_web),
    path('main_my_info',views.main_my_info),

    #快递小哥

    path('express_main',views.express_main),
    path('express_write_goods_info',views.express_write_goods_info),
    path('express_order_print',views.express_order_print)


]
