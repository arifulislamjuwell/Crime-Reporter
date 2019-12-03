from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import JsonResponse
from .models import Crimerepost
from authenticate.models import Profile
import smtplib
import os
import json
from django.contrib.auth.models import User
# Create your views here.
def emergency(request):
    if request.method == 'POST':
        details_list=[]
        pol_dic={
            'name':'',
            'position':'',
            'number':''
        }
        email_list=[]

        district= request.POST['district']
        phone= request.POST['phone']
        location=request.POST['location']

        crime_obj= Crimerepost()

        crime_obj.name= request.POST['name']
        crime_obj.phone=phone
        crime_obj.district= district
        crime_obj.location=location
        crime_obj.message= request.POST['message']
        crime_obj.save()

        list_polices_distric = Profile.objects.filter(district= district, type_of='police')
        for police in list_polices_distric:
            email_list.append(police.user.username)
            pol_dic['name']= police.fullname
            pol_dic['position']=police.position
            pol_dic['number']=police.phone
            details_list.append(pol_dic)

        EMAIL_ADDRESS='juwelariful1@gmail.com'
        EMAIL_PASS='' #password shoud be input
        with smtplib.SMTP('smtp.gmail.com',  587) as smtp:
             smtp.ehlo()
             smtp.starttls()
             smtp.ehlo()

             smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
             subject= 'CRIME REPORTER'
             body= 'I faced a crime with me at: '+ location + 'Please help me and immidiate contact with me, my number is:'+phone
             msg= f'Subject: {subject}\n\n{body}'
             for email in email_list:
                 smtp.sendmail(EMAIL_ADDRESS, email, msg)
        
        return HttpResponse(pol_dic)

def crime_report_list(request):
    templates='crime\crime_report_list.html'
    total_crime_list= Crimerepost.objects.filter(is_instant=False)

    try:
        if request.is_ajax():
            data_list=[]
            if request.method == "GET":
                id= request.GET['id']
                crime= Crimerepost.objects.filter(id=id).values('user','name','phone','district','location','message')
                for key,value in crime[0].items():
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
        return HttpResponse('error')

    return render(request,templates,{'crimereports':total_crime_list,})

def create_crime(request):
    templetes= 'crime\create_crime_report.html'

    if request.method == "POST":
        print('----------------------->')
        crime_report= Crimerepost()

        crime_report.user= request.user
        crime_report.name= request.POST['title']
        crime_report.phone= request.POST['phone']
        crime_report.district=request.POST['zilla']
        crime_report.message=request.POST['message']
        crime_report.location=request.POST['location']
        crime_report.is_instant=False
        crime_report.save()

        return redirect('crime_report')
    else:
        return render(request,templetes)