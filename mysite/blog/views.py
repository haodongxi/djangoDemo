from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog import models
# Create your views here.

def index(request):
    # return HttpResponse('haha')
    return render(request,'index.html')
def dealWith(request):
    # return HttpResponse(request.POST.get('name',None))
    return render(request,'dealWith.html',{'name':request.POST.get('name',None)})
