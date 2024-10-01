from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth  # Import User model for creating new users
from django.contrib import messages  # Import messages framework for displaying messages to the user
from django.contrib.auth import authenticate,login,logout #Handles user's credentials ,login,logout and authentications.
from django.contrib.auth.decorators import login_required #Handles accesibility of view.
from .models import *

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
       
         #check if password is same 
         
        if pass1 == pass2:
            if User.objects.filter(email=email).exists():   #check if email already registered
                messages.info(request,'email already exists!')
                return redirect('register')
            elif User.objects.filter(username=uname).exists():   # check if  same username exists 
                messages.info(request,'username already taken!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname,first_name=fname,last_name=lname, email=email, password=pass1)
                user.save()
                
                #log user in and redirect to settings page
                user_login = auth.authenticate(username=uname,password=pass1)
                auth.login(request,user)
                
                # create a profile object for the new user
                
                user_model=User.objects.get(username=uname)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('setting')
        else:
            messages.info(request,'password does not matched!!')
            return redirect('register')
        
            
    else:
        return render(request,'signup.html')  
            

#view for loginpage
def loginn(request):
    if request.method =='POST':
        uname=request.POST['username']
        pass1=request.POST['pass1']
        user = auth.authenticate(username=uname,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'credentials Invalid')
            return redirect('loginn')
    else:    
        return render(request,'loginn.html')



 #view for logoutpage
def logout(request):
    return redirect('home')

#view for index
def index(request):
    return render(request,'index.html')

def setting(request):
    return render(request,'settings.html')




