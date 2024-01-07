from django.contrib import admin
from django.urls import path
from DmsApp.views import *
urlpatterns = [
    path('',home,name='home'),
    path('progress/',progress,name='progress'),
    path('guidelines/',guidelines,name='guidelines'),
    path('solved/',solved,name='solved'),
]
