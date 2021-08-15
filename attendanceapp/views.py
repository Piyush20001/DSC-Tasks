from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import attendeeregistration
from django.contrib import messages




def myhome(request):
    return render(request, 'home.html')




def dashboard(request):
    workshops = workshopdetails.objects.all()
    return render(request, 'index.html' , {'workshops':workshops})




def loginn(request):
    if request.method=="POST":
       id=request.POST["username"]
       password=request.POST["password"]
       auth=authenticate(username=id,password=password)
       if auth is not None:
            login(request,auth)
            return HttpResponseRedirect("/dashboard")
       else:
            return HttpResponseRedirect("/login")
    else:
        return render (request, 'login.html')
def workshopregister(request,attendees):
    if workshopdetails.currentuserattending=="No":
        workshopdetails.currentuserattending=="Yes"
        myobj=get_object_or_404(workshopdetails,pk=attendees)
        myobj.NoofPeopleRegistered=myobj.NoofPeopleRegistered+1
        myobj.save()
    else: 
        messages.info(request, 'You have already registered for this Workshop')  

def register(request):
    if request.method=="POST":
        form = attendeeregistration(request.POST)
        if form.is_valid():
            userObj=form.cleaned_data
            fullname=userObj['fullname']
            username=userObj['username']
            email=userObj['email']
            batch=userObj['batch']
            enrollno=userObj['enrollno']
            branch=userObj['branch']
            password=userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')    
            else:
                raise forms.ValidationError('the Same Email or Username Already Exists.Please Login')
    else:
        form = attendeeregistration()
        
    return render(request, 'register.html', {'form' : form})        


def logout1(request):
    logout(request)
    return HttpResponseRedirect("/")