from django.urls import path,include 
from . import views

urlpatterns= [
    path('', views.myhome,name="myhome"),
    path('login',views.loginn,name="login"),
]