from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your views here.
def login(request):
    templates='auth\login.html'
    contex_error={'error_user':'Email or Password Is Incorrect'}

    if request.method=="POST":
        user =auth.authenticate(username= request.POST['email'], password= request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request,templates,contex_error)
    else:
        return render(request,templates)


def singup(request):
    templates='auth\singup.html'
    contex_user={'user_error':'This account already exist'}
    contex_password={'pass_error': 'Password doesnt match'}
    if request.method == "POST":
        if request.POST['password']== request.POST['password2']:
            try:
                users= User.objects.get(username=request.POST['email'])
                if users:
                    return render(request,templates,contex_user)
            except User.DoesNotExist:
                users= User.objects.create_user(request.POST['email'], password=request.POST['password'])
                profile= Profile.objects.get(user=users)
                try:
                    profile.type_of=request.POST['adminstration']
                except:
                    profile.type_of=request.POST['victim']
                profile.fullname=request.POST['fullname']
                profile.district=request.POST['dis']
                profile.phone=request.POST['number']
                profile.position=request.POST['choice1']
                profile.save()
                auth.login(request, users)
                return redirect('index')

        else:
            return render(request,templates,contex_password)
    else:
        return render(request,templates)


@login_required
def logout (request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')

def createProfile(request):
    templates= 'auth/createprofile.html'
    return render(request, templates)