from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

def adminLogin(request):
    if request.method == "POST":
        p_username  = "naseef"
        p_password = "1234"
        username = request.POST['username']
        password =  request.POST['password']
        if username == p_username and password:
            request.session['username'] = username
            messages.info(request, ' Loged in')
            return redirect(adminDashboard)
        else:
            messages.error(request, ' Wrong username/password!')
            return render(request, 'admin_login.html')   
    return render(request, 'admin_login.html')      
    
def adminDashboard(request):
    if request.session.has_key('username'):
        list = User.objects.all()
        return render(request, 'admin_dashboard.html',{'datas':list})
    else:
        return redirect('/adminlogin')    
def logout(request):
    if request.session.has_key('username'):
        request.session.flush()
        return redirect('/adminlogin')    
    else:
        pass
    return render(request, 'admin_login.html')     
def edit(request,id):
    user = User.objects.get(id=id)
    return render(request, 'edit.html',{'user':user})

def update(request,id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        user.email=email
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.password = password
        user.save();
        messages.success(request,"Updated Successfully")
        return redirect(adminDashboard)
    else:
        return redirect(adminDashboard)

def destroy(request, id):  
    user = User.objects.get(id=id)  
    user.delete()  
    messages.info(request,"Deleted Successfully")
    return redirect(adminDashboard)

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
    

def logoutuser(request):
    auth.logout(request)
    return redirect('/')