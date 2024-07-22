from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    login_count=request.COOKIES.get('login_count',0)
    return render(request,'index.html',{"login_count":login_count})

def user_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            response=redirect("index")
            login_count=int(request.COOKIES.get('login_count',0))+1
            response.set_cookie("login_count",login_count)
            return response
        else:
            return HttpResponse("Invalid")
    return render(request,"login.html")



