from django.shortcuts import render

# Create your views here.
def index(request):
    templates='index.html'
    return render(request, templates)
