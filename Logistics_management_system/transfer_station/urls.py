
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login_view),
    path('transform',views.transform_view),

]
