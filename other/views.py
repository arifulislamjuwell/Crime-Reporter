from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from bs4 import BeautifulSoup
import requests
import re
from csv import writer
from .models import Notice
from authenticate.models import Profile
from django.contrib.auth.models import User
from django.http import JsonResponse

def thana_Number(request):
    templates='other\\thanaNumber.html'
    thana=''
    response= requests.get('https://www.mediabangladesh.net/police-phone-number-bangladesh-thana-oc/')
    soup=BeautifulSoup(response.text, 'html.parser')
    post=soup.find('div',{'class': 'entry-content'}).findAll('p')
    for element in post:
         thana+= '\n' + ''.join(element.findAll(text = True))
    description=re.split(r'\d{11}', thana)
    reg=re.compile(r'\d{11}')
    number=reg.findall(thana)
    list=[]
    k=0
    while k< len(number):
        list.append(description[k]+'-'+number[k])
        k+=1
    return render(request, templates,{'aa':list})

def notice(request):
    templates= 'other\\notice.html'
    notice= Notice.objects.all()
    if request.method=="POST":
        district=request.POST.get('dis')
        if district:
            notice=notice.filter(area__district=district)
    profile=Profile.objects.get(user=request.user)
    return render(request, templates,{'notices':notice,'profile':profile})

def add_notice(request):
    templates= 'other\\add_notice.html'
    if request.method == "POST":
        user= request.user
        user_obj= get_object_or_404(User, username=user)
        profile= get_object_or_404(Profile, user= user_obj)
        notice= Notice()
        notice.crater= user
        notice.area= profile
        notice.title= request.POST['title']
        notice.expire_time=request.POST['ex_date']
        notice.descrp=request.POST['description']
        notice.exact_location=request.POST['location']
        notice.save()

        return redirect('notice')
    else:
        return render(request, templates,{})

def show_notice(request):
    try:
        if request.is_ajax():
            data_list=[]
            if request.method == "POST":
                id= request.POST['id']
                notice= Notice.objects.filter(id=id).values('crater','area__district','title','created_time','descrp','exact_location')
                for key,value in notice[0].items():
                    data_list.append(value)
                user_id=data_list[0]
                user_name=Profile.objects.filter(user__id=user_id).values('fullname')
                data_list[0]=user_name[0]['fullname']
                print(data_list)
                context={
                    'data':data_list
                }
                return JsonResponse(context ,safe= False)
    except Exception as e:
        print(e)
        return render (request,'crime\crime_report_list.html' )