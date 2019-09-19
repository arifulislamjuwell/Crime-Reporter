from django.shortcuts import render

# Create your views here.
def login(request):
    templates='auth\login.html'
    return render(request,templates)
