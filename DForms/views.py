from django.shortcuts import render
from django.http import HttpResponse
from DForms.forms import *
from DForms.models import *
# Create your views here.

def django_forms(request):
    SUO=SignUp()
    d={'SUO':SUO}
    if request.method=='POST':
        DSO=SignUp(request.POST)
        if DSO.is_valid():
            return HttpResponse('Data gathering finished successfully')
    return render(request,'django_forms.html',d)

def django_topic(request):
    TO=Topic()
    d={'TO':TO}
    if request.method=='POST':
        TDO=Topic(request.POST)
        if TDO.is_valid():
            return HttpResponse('Data gathering finished successfully..!!')
    return render(request,'django_topic.html',d)

def django_page(request):
    WO=Webpage()
    d={'WO':WO}
    if request.method=='POST':
        WDO=Webpage(request.POST)
        if WDO.is_valid():
            return HttpResponse('Data gathering finished successfully..!!')
    return render(request,'django_page.html',d)
