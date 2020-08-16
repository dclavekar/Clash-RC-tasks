from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile

def signup(request):
    if(request.method=="POST"):
        username=request.POST['username']
        if(User.objects.filter(username=username).exists()):
            messages.error(request,'This username is already taken')
            return render(request,'signup.html')
        else:
            password1=request.POST['password1']
            password2 = request.POST['password2']
            if(password1==password2):
                firstname=request.POST['firstname']
                lastname = request.POST['lastname']
                phoneno = request.POST['phoneno']
                email = request.POST['email']

                user=User.objects.create_user(username=username,email=email,password=password1,first_name=firstname,last_name=lastname)
                '''if(len(user)==0):
                    messages.error(request, 'please fill all the fields')
                    return render(request,'signup.html')'''
                user.save()
                profile=Profile(user=user, phoneno=phoneno)
                profile.save()
                messages.info(request,'User successfully created')
                return render(request, 'loggedin.html', {'message': 'You are successfully logged in'})


            else:
                messages.error(request, 'Both the entered passwords dont match')
                return render(request, 'signup.html')

    return render(request,'signup.html',{'message':'Welcome'})

def views_login(request):
    if(request.method== "POST"):
        username=request.POST['username']
        password=request.POST['password']
        temp=authenticate(request,username=username, password= password)
        if temp is not None:
            login(request,temp)
            return render(request,'loggedin.html', {'message': 'You are successfully logged in'})
        else:
            return render(request,'login.html',{'message':'Invalid Credentials'})
    return render(request, 'login.html')

def views_loggedin(request):
    return render(request,'loggedin.html',{'message':'please log in first'})

def views_logout(request):
    logout(request)
    return redirect('login.html')
















