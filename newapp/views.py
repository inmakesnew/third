from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
# Create your views here#
def login(request):
    if request.method=='POST':
       username=request.POST['username']
       Password=request.POST['Password']
       user=auth.authenticate(username=username,Password=Password)
       if user is not None:
          auth.login(request,user)
          return redirect('/')
       else:
          messages.info(request,"invalid newapp")
          return redirect('login')

    return render(request, "login.html")
def register(request):
    if request.method=='POST':
        username= request.POST['username']
        First_name=request.POST['First_name']
        Last_name= request.POST['Last_name']
        Email= request.POST['Email']
        Password= request.POST['Password']
        f= request.POST['Confirm Password']
        if Password==f:
            if User.objects.filter(username=username).exists():
               messages.info(request,"Username Taken")
               return redirect('register')
            elif User.objects.filter(Email=Email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
               user=User.objects.create_user(username=username,Password=Password,First_name=First_name,Last_name=Last_name,Email=Email)
               user.save();
               return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')