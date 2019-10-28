from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Crimerepost
from authenticate.models import Profile

# Create your views here.
def emergency(request):
    if request.method == 'POST':
        email_list=[]
        crime_obj= Crimerepost()
        district= request.POST['district']
        crime_obj.name= request.POST['name']
        crime_obj.phone= request.POST['phone']
        crime_obj.district= district
        crime_obj.location= request.POST['location']
        crime_obj.message= request.POST['message']
        crime_obj.save()

        obj = Profile.objects.filter(district= district, type_of='police')
        for i in obj:
            email_list.append(i.user.username)
            print(email_list)
        return HttpResponse('')