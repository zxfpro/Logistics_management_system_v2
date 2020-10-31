
from django.urls import path
from . import views

urlpatterns = [

    path('appstart',views.appstart_view),
    path('wayBill_main',views.wayBill_main),
    path('main_my_info',views.main_my_info),
]
