from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    #return HttpResponse("<h1> Hey i am the future of india </h1>")
    report=Report.objects.all()
    context={'report':report}
    return render(request,'home.html',context)
def progress(request):
    return render(request,'progress.html')

def solved(request):
    return render(request,'solved.html')

def guidelines(request):
    return render(request,'guidelines.html')