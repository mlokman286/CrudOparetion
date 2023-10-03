from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from myapp.models import Employes

# Create your views here.
def signupPage(request):
    if request.method =="POST":
        uname =request.POST.get('username')
        mail =request.POST.get('email')
        pass1 =request.POST.get('password1')
        pass2 =request.POST.get('password2')
        if pass1 !=pass2:
            return HttpResponse('your password is not match')
        else:
            user = User.objects.create_user(username=uname,email=mail,password = pass1)
            user.save()
            return redirect('loginPage')
        
    return render(request,'signup.html')

def loginPage(request):
    if request.method =="POST":
        uname =request.POST.get('username')
        psd =request.POST.get('pass')
        user = authenticate(request, username=uname, password=psd)
        if user is not None:
            return redirect('homePage')
            
        else:
            return redirect('loginPage')

    return render(request,'login.html')

def homePage(request):
    user = request.user
    emp = Employes.objects.all()
    return render(request,'home.html',{'user':user,'emp':emp})

def addPage(request):
    if request.method =="POST":
        adName =request.POST.get('name')
        ademail =request.POST.get('email')
        adsemister =request.POST.get('semister')
        addbatch =request.POST.get('batch')
        adAddress =request.POST.get('address')
        adPhone =request.POST.get('phone')

        emp=Employes(
            name=adName,
            email=ademail,
            semester=adsemister,
            batch=addbatch,
            phone=adPhone,
            address=adAddress,
        )
        emp.save()
        return redirect('homePage')
    
def editPage(request):

    emp=Employes.objects.all()
    context = {
        'emp':emp
    }
    return render(request,'home.html',context)

def updatePage(request,id):
    if request.method =="POST":
        adName =request.POST.get('name')
        ademail =request.POST.get('email')
        adsemister =request.POST.get('semister')
        addbatch =request.POST.get('batch')
        adAddress =request.POST.get('address')
        adPhone =request.POST.get('phone')

        emp=Employes(
            id = id,
            name=adName,
            email=ademail,
            semester=adsemister,
            batch=addbatch,
            phone=adPhone,
            address=adAddress,
        )
        emp.save()
        return redirect('homePage')
    
def deletePage(request,id):
    emp = Employes.objects.filter(id=id)
    emp.delete()
    return redirect('homePage')