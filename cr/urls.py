
from django.urls import path,include
from .views import *

urlpatterns = [
    path('emergeny/', emergency, name='emergency' ),
    path('crime_report_list/', crime_report_list, name= 'crime_report'),
    path('add-crime_report/', create_crime, name='create_crime'),

]