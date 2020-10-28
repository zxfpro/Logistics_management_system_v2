from django.shortcuts import render

# Create your views here.


def login_view(request):
    if request.method =='GET':
        render(request,'transfer_station/login_view.html')
    elif request.method =='POST':


        render(request, 'transfer_station/login_view.html',locals())


def transform_view(request):
    if request.method == 'GET':
        render(request, 'transfer_station/transform_view.html')
    elif request.method == 'POST':

        render(request, 'transfer_station/transform_view.html', locals())

