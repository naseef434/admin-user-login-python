from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

def adminLogin(request):
    return render(request,'admin_login.html')

def adminDashboard(request):
    # return HttpResponse("Hello naseef")
    return render(request, 'admin_dashboard.html')

def userRegistration(request):
    #check request method post
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        #check user name already exist in model
        if User.objects.filter(username=username).exists():
            messages.error(request, ' User name already exist')
            return render(request, 'registration.html')
        else:
            #inserting data in to User model
            user = User.objects.create_user(username=username,email=email, first_name=first_name, last_name=last_name,password=password)
            user.save();
            return redirect(userLogin)
    else:
        return render(request, 'registration.html')

def userLogin(request):
    #check authenticated user loged in or not
    if request.user.is_authenticated:
        return redirect(userDashboard)
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        #check user entred username and password
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(userDashboard)
        else:
            messages.error(request, ' Wrong username/password!')
            return redirect('/')
    else:    
        return render(request, 'user_login.html' )


def userDashboard(request):
    #check if authenticated user logged in 
    if request.user.is_authenticated:
        return render(request,'user_dashboard.html')
    else:
        return redirect(userLogin)    
    
def simple(request):
    return render(request, 'simple.html')

def logoutuser(request):
    #auth user logout
    auth.logout(request)
    return redirect('/')