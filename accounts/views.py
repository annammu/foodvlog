from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            print("logged ")
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalied details")
            return redirect('login')
    else:
        return render(request,"login.html")
def register(request):
    if request.method=="POST":

        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username allready taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request, "email allready taken")
                 return redirect('register')
            else:

               user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password1,email=email)
               user.save()
               messages.success(request,f'account created')


        else:
             print("password not matched")
             return redirect('register')

        return redirect('/')
    else:

        return render(request,'registeration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
