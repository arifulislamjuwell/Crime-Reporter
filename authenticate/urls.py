from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('singup/', views.singup, name='singup'),
    path ('logout/',views.logout, name= 'logout'),
]
