
from django.urls import path
from . import views

urlpatterns = [

    path('appstart',views.appstart_view),
    path('recipient',views.recipient_view),
    path('sender',views.sender_view),
    path('address_page',views.address_page_view)
]
