from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import details
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=="GET":
        emptyform=details()
        return render(request,'accounts/register.html',{'emptyform':emptyform})
    if request.method=="POST":
        detailform=details(request.POST)
        if detailform.is_valid()==True:
            uname=detailform.cleaned_data['username']
            pwd=detailform.cleaned_data['password']
            email=detailform.cleaned_data['email']
            uobj=User.objects.create(username=uname,password=pwd,email=email)
            uobj.set_password(pwd)
            uobj.save()
            return redirect('loginurls')
        else:
             return render(request,'accounts/register.html',{'emptyform':detailform})
def login1(request):
    if request.method=="GET":
        return render(request,'accounts/login.html')
    if request.method=="POST":
        uname=request.POST['user']
        pwd=request.POST['password']
        obj=authenticate(request,username=uname,password=pwd)
        if obj is None:
            return redirect("loginurls")
        else:
            login(request,obj)
            return redirect("homeurls")
def logout1(request):
    logout(request)
    return redirect('loginurls')
from django.shortcuts import render
@login_required(login_url='loginurls')
def about(request):
    return render(request, 'accounts/about.html')
@login_required(login_url='loginurls')
def contact(request):
    return render(request, 'accounts/contact.html')
    
