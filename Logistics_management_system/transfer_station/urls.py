
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login_view),
    path('transform_view',views.transform_view),

]
