from django.urls import path,include 
from . import views

urlpatterns= [
    path('', views.myhome,name="myhome"),
    path('login',views.loginn,name="login"),
    path('register',views.register,name="register"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout', views.logout1, name = "logout"),
    path('workshopregister/<str:attendees>', views.workshopregister, name = "workshopregister"),
]