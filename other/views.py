from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from bs4 import BeautifulSoup
import requests
import re
from csv import writer
from .models import Notice
from authenticate.models import Profile
from django.contrib.auth.models import User

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
    return render(request, templates)

def add_notice(request):
    templates= 'other\\add_notice.html'
    if request.method == "POST":
        print('----------------------->')
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