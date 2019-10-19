from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re
from csv import writer

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
