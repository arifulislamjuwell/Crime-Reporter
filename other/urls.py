from . import views
from django.urls import path

urlpatterns = [
    path('492_thana_details/',views.thana_Number, name='thanaNumber'),
    path('notice/', views.notice, name= 'notice'),
    path('add-notice/', views.add_notice, name='add_notice'),
    path('show-notice/', views.show_notice,name='show_notice'),
]
