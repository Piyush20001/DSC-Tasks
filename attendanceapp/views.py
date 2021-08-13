from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .models import *




def myhome(request):
    return render(request, 'home.html')


def loginn(request):
    if request.method=="POST":
       id=request.POST["username"]
       password=request.POST["password"]
       auth=authenticate(username=id,password=password)
       if auth is not None:
            login(request,auth)
            return HttpResponseRedirect("/")
       else:
            return HttpResponseRedirect("/login")
    else:
        return render (request, 'login.html')
