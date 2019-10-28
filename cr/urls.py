
from django.urls import path,include
from .views import emergency

urlpatterns = [
    path('emergeny/', emergency, name='emergency' ),

]