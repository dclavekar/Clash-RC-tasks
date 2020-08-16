from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages


def page1(request):
    if(request.method=="POST"):
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        gender = request.POST['gender']
        username=request.POST['email']
        password=None


        if(User.objects.filter(email=email).exists()):
            print('user already exists')
            messages.info(request, "email adress already taken")
        else:
            user = User.objects.create_user(username=email, email= email, password=None, first_name= firstname, last_name=lastname)
            user.save()
            profile=Profile(user=user, phoneno=phoneno, gender=gender)
            profile.save()


        return render(request, 'page1.html')

    return render(request, 'page1.html')

def page2(request):
    if(request.method=="POST"):
        email=request.POST['email']
        '''if(User.objects.filter(email=email).exists()):
            #user1=User.objects.filter(email=email)
            profile=Profile.objects.get(email=email)
            #messages.info(request,"User found")
            content={'profile':profile}
            return render(request,'page3.html',content)
        else:
            messages.info(request,"Sorry no user found with entered email")
            return render(request,'page4.html')'''

        try:
            user= User.objects.get(email=email)
            profile=Profile.objects.get(user=user)
            content={'message': 'Found User', 'profile':profile}
            return render(request,'page3.html',content)

        except :
            return render(request,'page4.html', {'message': 'sorry user not found'})
    return render(request, 'page2.html')