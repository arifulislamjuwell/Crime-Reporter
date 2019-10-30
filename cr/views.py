from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Crimerepost
from authenticate.models import Profile
import smtplib
import os

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