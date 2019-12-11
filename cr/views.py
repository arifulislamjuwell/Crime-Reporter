from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import JsonResponse
from .models import Crimerepost,Comment
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
        crime_obj.is_instant=True
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
    try:
        profile=get_object_or_404(Profile, user=request.user)
    except Exception as e:
        return render(request,templates)
    total_crime_list= Crimerepost.objects.filter(is_instant=False)

    if request.method=="POST":
        district=request.POST.get('dis')
        if district:
            total_crime_list=total_crime_list.filter(district=district)
    return render(request,templates,{'crimereports':total_crime_list,'profile':profile})

def create_crime(request):
    templetes= 'crime\create_crime_report.html'

    if request.method == "POST":
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

def show_crime(request):
    try:
        if request.is_ajax():
            data_list=[]
            if request.method == "POST":
                id= request.POST['id']
                crime= Crimerepost.objects.filter(id=id).values('user','name','phone','district','location','message','date')
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
        return render (request,'crime\crime_report_list.html' )

def own_crime(request):
    try:
        own_crime= Crimerepost.objects.filter(user= request.user)
        return render(request,'crime\own_crime.html',{'crimes':own_crime})
    except Exception as e:
        own_crime='you have no created crime'
        return render(request,'crime\own_crime.html')

def delete_crime(request):
    try:
        id=request.POST.get('id')
        get_object_or_404(Crimerepost, id=id).delete()
        return HttpResponse('')
    except Exception as e:
        print(e)

def search_officer(request):
    try:
        id=request.POST.get('id')
        crime= get_object_or_404(Crimerepost, id=id)
        officer_list=[]
        profile= Profile.objects.filter(type_of="police", district=crime.district).values('id','fullname','position')
        for i in profile:
            dic={
            }
            dic['id']=i['id']
            dic['name']=i['fullname']
            dic['position']=i['position']
            officer_list.append(dic)

        context={
            'data':officer_list,
            'id':id
        }
        return JsonResponse(context, safe=False)
    except Exception as e:
        print(e)


def refer_crime(request):
    try:
        user_id=request.POST.get('user_id')
        crime_id=request.POST.get('crime_id')
        print(user_id)
        print(crime_id)
        user= get_object_or_404(Profile, id=user_id)
        crime=get_object_or_404(Crimerepost, id=crime_id)
        print(user)
        print(crime)
        crime.refer_user=user
        crime.save()
        return JsonResponse({}, safe=False)

    except Exception as e:
        print(e)

def reply_crime(request):
    if request.is_ajax():
        id = request.GET['id']
        try:
            crime = get_object_or_404(Crimerepost, id=id)
            reply_all = Comment.objects.filter(name=crime).values("cerated_time", "user__username", 'body')
            reply_all = list(reply_all)
        except Exception as e:
            reply_all = 'No Reply'
            logger.info(str(e))
            print(e)
        return JsonResponse(reply_all, safe=False)

    else:
        return Response('')

def create_comment(request):
    if request.is_ajax():
        id = request.POST['id']
        body= request.POST['body']
        crime= get_object_or_404(Crimerepost, id=id)
        c_comment=Comment()
        c_comment.user=request.user
        c_comment.name=crime
        c_comment.body=body
        c_comment.save()
        return HttpResponse('create')

def solved_crime(request):
    if request.is_ajax():
        id = request.GET['id']
        Crimerepost.objects.filter(id=id).update(is_solved=True)
        return HttpResponse('success')

def refer_list(request):
    profile=Profile.objects.get(user=request.user)
    crime=Crimerepost.objects.filter(refer_user=profile)
    return render(request,'crime/refer_crime.html',{'crimes':crime})

def take_under(request):
    if request.is_ajax():
        id = request.POST['id']
        crime_name=Crimerepost.objects.get(id=id)
        if not crime_name.take_under:
            profile=Profile.objects.get(user=request.user)
            Crimerepost.objects.filter(id=id).update(take_under=profile)
            mes= 'crime "{}" taken by "{}"'.format(crime_name.name, profile.fullname)
            return HttpResponse(mes)
        else:
            return HttpResponse('alredy taken')