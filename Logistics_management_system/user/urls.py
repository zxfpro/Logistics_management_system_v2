
from django.urls import path
from . import views

urlpatterns = [

    path('appstart',views.appstart_view),
    path('login', views.login),
    path('register', views.register),
    path('check_user',views.check_user),
]
