from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User  # Import User model for creating new users
from django.contrib import messages  # Import messages framework for displaying messages to the user
from django.contrib.auth import authenticate,login,logout #Handles user's credentials ,login,logout and authentications.
from django.contrib.auth.decorators import login_required #Handles accesibility of view.
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator #divide items into pages
import json
from django.db import IntegrityError
from .models import *

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        emailid=request.POST.get('email')
        profile = request.FILES.get("profile")
        print(f"--------------------------Profile: {profile}----------------------------")
        cover = request.FILES.get('cover')
        print(f"--------------------------Cover: {cover}----------------------------")
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        
        if pass1!= pass2:
            return render(request, "templates/signup.html", {
                "message": "Passwords must match."
            })
            
            
            #attempt to create new user
        try:
            user = User.objects.create_user(uname, emailid, pass1)
            user.first_name = fname
            user.last_name = lname
            if profile is not None:
                user.profile_pic = profile
            else:
                user.profile_pic = "profile_pic/blank-profile-picture.png"
            user.cover = cover           
            user.save()
            Follower.objects.create(user=user)
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponse(request,'index')
    else:
        return render(request,'signup.html')
    

#view for loginpage

def loginn(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["pass1"]
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return HttpResponse
            return render(request,'loginn.html')
        else:
            return render(request,'loginn.html',{
            "message": "Invalid username and/or password."
        })
    else:
        return render(request,'loginn.html')
  
def logout(request):
    return HttpResponse(request,'index') 

#view for mainpage

def index(request):
    return render(request,'index.html')
   