from django.shortcuts import render







def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        emailid=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        print(uname,emailid,fname,lname,pass1,pass2)
        
  
    return render(request,'signup.html')

def loginn(request):
    return render(request,'loginn.html')