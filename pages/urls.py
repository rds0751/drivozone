from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('about',views.about,name ='about'),
    path('car_service',views.carservice,name ='car_service'),
    path('Bike_service',views.bikeservice,name ='bike_service'),
    path('commerical_service',views.commericalservice,name ='commerical_service'),
   path('pcv_service',views.pcvservice,name ='pcv_service'),

]
