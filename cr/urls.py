
from django.urls import path,include
from . import views
urlpatterns = [
    path('emergeny/',views.emergency,name='emergency' ),

]