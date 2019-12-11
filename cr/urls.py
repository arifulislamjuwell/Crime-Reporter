
from django.urls import path,include
from .views import *

urlpatterns = [
    path('emergeny/', emergency, name='emergency' ),
    path('crime-report-list/', crime_report_list, name= 'crime_report'),
    path('add-crime_report/', create_crime, name='create_crime'),
    path('show-crime/',show_crime, name='show_crime'),
    path('own-crime/',own_crime, name='own_created_crime'),
    path('delete-crime/',delete_crime, name='delete_crime'),
    path('search-officer/', search_officer, name='src_officer'),
    path('refer-crime/',refer_crime, name='refer_crime'),
    path('reply-crime/',reply_crime, name='reply_crime'),
    path('create-comment/',create_comment, name='create_comment'),
    path('solve/',solved_crime, name='solved'),
    path('refer-list/',refer_list, name='refer_list'),
    path('take-under',take_under, name='take_under'),
]