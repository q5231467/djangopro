from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    # context          = {}
    # context['hello'] = 'Hello World!'
    views_name = "test教程"
    views_list = ["test教程1","test教程2","test教程3"]
    return render(request, 'runoob.html', {"name":views_name,"views_list":views_list})