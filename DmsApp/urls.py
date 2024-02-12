from django.contrib import admin
from django.urls import path
from DmsApp.views import *
urlpatterns = [
    path('',home,name='home'),
    path('progress/',progress,name='progress'),
    path('guidelines/',guidelines,name='guidelines'),
    path('register/',registerPage,name='register'),
    path('login/',userLogin,name='login'),
    path('logout/',logoutuser,name='logout'),
    path('report/',createReport,name='report'),
    path('solved/',solved,name='solved'),
    path('signup_vol/',signup_vol,name='signup_vol'),
    path('signup_org/',signup_org,name='signup_org'),
    path('profile/',profile,name='profile'),
    path('editprofile/',edit_profile,name='edit_profile'),
    path('dashboard_vol/',dashboard_vol,name='dashboard_vol'),
    path('dashboard_org/',dashboard_org,name='dashboard_org'),
    path('add_resource/',add_resource,name='add_resource'),
    path('resource/',resource,name='resource'),
    path('accept_report/<int:report_id>/', accept_report, name='accept_report'),
    path('mark_solve/<int:report_id>/',mark_solve,name='mark_solve'),
    

    #path('login/',login_user,name='login'),
    
    #path('user/',userpage,name='user'),
]
