
from django.urls import path
from . import views

urlpatterns = [

    path('appstart',views.appstart_view),
]
