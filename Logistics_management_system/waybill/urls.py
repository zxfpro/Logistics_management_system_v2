
from django.urls import path
from . import views

urlpatterns = [

    path('appstart',views.appstart_view),
    path('wayBill_main',views.wayBill_main),
]
