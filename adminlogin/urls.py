from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.userLogin),
    path('registration/',views.userRegistration, name="registration"),
    path('dashboard/',views.userDashboard, name="dashboard"),
    path('adminlogin/',views.adminLogin, name="adminlogin"),
    path('dashboard1/',views.adminDashboard),
    path('logoutuser/',views.logoutuser),
    # path('userLogin/',views.userLogin, name="userLogin")

   
]