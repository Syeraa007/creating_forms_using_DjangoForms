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
            DSignUp.objects.get_or_create(name=DSO.cleaned_data['name'],age=DSO.cleaned_data['age'],course=DSO.cleaned_data['course'],email=DSO.cleaned_data['email'],password=DSO.cleaned_data['password'],gender=DSO.cleaned_data['gender'],address=DSO.cleaned_data['address'])[0].save()
            return HttpResponse('Data gathering finished successfully')
    return render(request,'django_forms.html',d)

def django_topic(request):
    TO=Topic()
    d={'TO':TO}
    if request.method=='POST':
        TDO=Topic(request.POST)
        if TDO.is_valid():
            DTopic.objects.get_or_create(topic_name=TDO.cleaned_data['topic'])[0].save()
            return HttpResponse('Data gathering finished successfully..!!')
    return render(request,'django_topic.html',d)

def django_page(request):
    WO=Webpage()
    d={'WO':WO}
    if request.method=='POST':
        WDO=Webpage(request.POST)
        TDO=DTopic(request.POST['topic'])
        if WDO.is_valid():
            DWebpage.objects.get_or_create(topic_name=TDO,name=WDO.cleaned_data['name'],url=WDO.cleaned_data['url'])[0].save()
            return HttpResponse('Data gathering finished successfully..!!')
    return render(request,'django_page.html',d)

def form_show(request):
    DSO=DSignUp.objects.all()
    DTO=DTopic.objects.all()
    DWO=DWebpage.objects.all()
    d={'DSO':DSO,'DTO':DTO,'DWO':DWO,'DAO':DAO}
    return render(request,'form_show.html',d)