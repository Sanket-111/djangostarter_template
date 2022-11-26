from django import http
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
# Create your views here.
# register

# This is inbuilt Django Form.
"""def register(request):
    form=UserCreationForm
    if request.method=='POST':
        regform=UserCreationForm(request.POST)
        if regform.is_valid():
            regform.save()
            messages.success(request,'User succesfully Register.')
    return render(request,'register.html',{'form':form})
    """
    

def login(request):
    if request.method == 'POST':
        if request.POST.get('signin'):
            uname=request.POST['uname']
            pword=request.POST['pword']

            user=auth.authenticate(username=uname,password=pword)
            if user is not None:
                auth.login(request,user)
                return render(request,'home.html')

            else:
                messages.warning(request,'Invalid Credentials.')
                return render(request,'register.html')

        if request.POST.get('signup'):
            username=request.POST['username']
            email=request.POST['email']
            password1=request.POST['password1']
            password2=request.POST['password2']

            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.warning(request,'User already Exists.')
                    return render(request,'register.html')
                elif User.objects.filter(email=email).exists():
                    messages.warning(request,'Email already Exists.')
                    return render(request,'register.html')

                else:
                    user=User.objects.create_user(username=username,password=password1,email=email)
                    user.save()
                    messages.success(request,'User succesfully Register.')
                    return render(request,'register.html') 

            else:
                messages.warning(request,'Password not matching.')  
                return render(request,'register.html') 
    else:
        return render(request,'register.html')        

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')    