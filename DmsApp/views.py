from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.views.generic import FormView,CreateView

# Create your views here.
@unauthenticated_user
def registerPage(request):
    return render(request,'register.html')
@unauthenticated_user
def signup_org(request):
    registered = False
    if request.method == 'POST':
        form = CombinedOrgForm(request.POST)
        if form.is_valid():
            # Create and save the User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            
            # Create and save the Organization
            organization = Organization.objects.create(
                org_name=user,
                domain=form.cleaned_data['domain'],
                location=form.cleaned_data['location'],
                level=form.cleaned_data['level']
            )
            organization.save()

            registered = True
            return redirect('/login/')
    else:
        form = CombinedOrgForm()

    context = {'form': form, 'registered': registered}
    return render(request, 'signup_org.html', context)

@unauthenticated_user
def signup_vol(request):
    registered = False
    if request.method == 'POST':
        form = CombinedVolForm(request.POST)
        if form.is_valid():
            # Create and save the User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            
            # Create and save the Volunteer
            volunteer = Volunteer.objects.create(
                vol_name=user,
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                skills=form.cleaned_data['skills'],
                city=form.cleaned_data['city'],
                org_name=form.cleaned_data['org_name']
            )
            volunteer.save()

            registered = True
            return redirect('/login/')
    else:
        form = CombinedVolForm()

    context = {'form': form, 'registered': registered}
    return render(request, 'signup_vol.html', context)

@unauthenticated_user
def userLogin(request):
    invalidlogin=False
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request, user)
            user = request.user
            if hasattr(user, 'organization'):
                return redirect('dashboard_org')
            else:
                return redirect('dashboard_vol')
            #return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request,'login.html',context)
    return render(request,'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')

def home(request):
    #return HttpResponse("<h1> Hey i am the future of india </h1>")
    report=Report.objects.all()
    report=report.filter(status='reported')
    context={'report':report}

    return render(request,'home.html',context)
@login_required(login_url='login')
def dashboard_vol(request):
    user = request.user
    user_type = 'volunteer'
    profile_info = Volunteer.objects.get(vol_name=user)
    report=Report.objects.all()
    report=report.filter(status='reported')
    context = {'user_type': user_type, 'profile_info': profile_info,'report':report}
    return render(request,'dashboard_vol.html',context)

@login_required(login_url='login')
def dashboard_org(request):
    user = request.user
    user_type = 'organization'
    profile_info = Organization.objects.get(org_name=user)
    report=Report.objects.all()
    report=report.filter(status='reported')
    context = {'user_type': user_type, 'profile_info': profile_info,'report':report}
    return render(request,'dashboard_org.html',context)

#@login_required(login_url='login')
def progress(request):
    report=Report.objects.all()
    report=report.filter(status='in_progress')
    context={'report':report}
    return render(request,'progress.html',context)

#@login_required(login_url='login')
def solved(request):
    report=Report.objects.all()
    report=report.filter(status='solved')
    context={'report':report}
    return render(request,'solved.html',context)

#@login_required(login_url='login')
def guidelines(request):
    return render(request,'guidelines.html')

#@login_required(login_url='login')
def createReport(request):
    form=ReportForm()
    context={'form':form}
    if request.method =='POST':
        form=ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')    
        #print('printing post:' ,request.POST)
    return render(request,'report.html',context)


@login_required(login_url='login')
def accept_report(request, report_id):
    user = request.user
    report = Report.objects.get(id=report_id)
    vol=Volunteer.objects.get(vol_name=user)
    # Check if the current user is the volunteer and the report is in 'reported' status
    if request.user.volunteer and report.status == 'reported':
        report.status = 'in_progress'
        report.volunteer = vol
        report.save()
        messages.success(request, 'Report accepted and set to In Progress.')
    else:
        messages.error(request, 'Unable to accept the report.')

    return redirect('dashboard_vol')

@login_required(login_url='login')
def mark_solve(request,report_id):
    report=Report.objects.get(id=report_id)
    volunteer = report.volunteer
    user = request.user
    if volunteer and request.user == volunteer.vol_name and report.status == 'in_progress':
        report.status = 'solved'
        report.save()
        messages.success(request, 'Report accepted and set to In Progress.')
    else:
        messages.error(request, 'Unable to accept the report.')

    return redirect('dashboard_vol')


@login_required(login_url='login')
def resource(request):
    all_rec=Resources.objects.all()
    context={'resource' : all_rec}
    return render(request,'resource.html',context)

@login_required(login_url='login')
def volunteers(request):
    user = request.user
    profile_info = Volunteer.objects.get(vol_name=user)
    org=profile_info.org_name
    vol=Volunteer.objects.filter(org_name=org).exclude(vol_name=user)
    contex={ 'vol':vol, 'org':org }
    return render(request,'associated_volunteers.html',contex)

def add_resource(request):
    form=Add_Resource()
    context={'form':form}
    if request.method =='POST':
        form=Add_Resource(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/resource/')    
        #print('printing post:' ,request.POST)
    return render(request,'add_resource.html',context)

def userpage(request):
    return render(request,'user.html')
@login_required(login_url='login')
def profile(request):
    user = request.user

    if hasattr(user, 'organization'):
        user_type = 'organization'
        profile_info = Organization.objects.get(org_name=user)
    else:
        user_type = 'volunteer'
        profile_info = Volunteer.objects.get(vol_name=user)

    context = {'user_type': user_type, 'profile_info': profile_info}
    return render(request, 'profile.html', context)
from django.contrib.auth.forms import UserChangeForm

@login_required(login_url='login')
def edit_profile_org(request):
    user = request.user
    org =Organization.objects.get(org_name=user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        org_form = UpdateOrgForm(request.POST, instance=org)
        if user_form.is_valid() and org_form.is_valid():
            user_form.save()
            org_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=user)
        org_form = UpdateOrgForm(instance=org)

    context = {'user_form': user_form, 'org_form': org_form}
    return render(request, 'edit_profile_org.html', context)

@login_required(login_url='login')
def edit_profile_vol(request):
    user = request.user
    volunteer =Volunteer.objects.get(vol_name=user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        vol_form = UpdateVolForm(request.POST, instance=volunteer)
        if user_form.is_valid() and vol_form.is_valid():
            user_form.save()
            vol_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=user)
        vol_form = UpdateVolForm(instance=volunteer)

    context = {'user_form': user_form, 'vol_form': vol_form}
    return render(request, 'edit_profile_vol.html', context)
