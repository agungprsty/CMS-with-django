import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render

from student_management_app.EmailBackEnd import EmailBackEnd


# Create your views here.
def showDemoPage(request):
    return render(request,"demo.html")

def LoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed<h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type=="2":
                return HttpResponse("<h2>Login To Staffs!<h2>"+str(user.user_type))
            else:
                return HttpResponse("<h2>Login To Students!<h2>"+str(user.user_type))
        else: 
            messages.error(request,"Invalid Login Details!")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" Usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First!")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
