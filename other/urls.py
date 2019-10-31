from . import views
from django.urls import path

urlpatterns = [
    path('492_thana_details/',views.thana_Number, name='thanaNumber'),
    path('notice/', views.notice, name= 'notice'),
]
