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
"""
@unauthenticated_user
def registerPage(request):
    form=UserForm()
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Acount is created for '+user)
            return redirect('/login/') 
    context={'form':form}
    return render(request,'register.html',context)

@unauthenticated_user
def loginPage(request):
    context={}
    if request.method == "POST":
        username=request.POST.get('username')#bcoz html ma form ma name=username
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request,'login.html',context)
    return render(request,'login.html')

 """
@unauthenticated_user
def registerPage(request):
    return render(request,'register.html')
@unauthenticated_user
def signup_org(request):
    registered=False
    if request.method=='POST':
        org=Org_Form(request.POST)
        org_add=Org_AddForm(request.POST)
        if org.is_valid() and org_add.is_valid():

            temp_org=org.save()
            temp_org.set_password(temp_org.password)
            temp_org.save()

            temp_add=org_add.save(commit=False)
            temp_add.org_name=temp_org
            temp_add.save()

            registered=True
            return redirect('/login/')
    else:
        org=Org_Form()
        org_add=Org_AddForm()

    context={'org':org , 'org_add':org_add,'registered':registered}
    return render(request,'signup_org.html',context) 
@unauthenticated_user
def signup_vol(request):
    registered=False
    if request.method=='POST':
        vol=Vol_Form(request.POST)
        vol_add=Vol_AddForm(request.POST)
        if vol.is_valid() and vol_add.is_valid():

            temp_vol=vol.save()
            temp_vol.set_password(temp_vol.password)
            temp_vol.save()

            temp_add=vol_add.save(commit=False)
            temp_add.vol_name=temp_vol
            temp_add.save()

            registered=True
            return redirect('/login/')
    else:
        vol=Vol_Form()
        vol_add=Vol_AddForm()

    context={'vol':vol , 'vol_add':vol_add,'registered':registered}
    return render(request,'signup_vol.html',context) 

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
    report = Report.objects.get(id=report_id)
    # Check if the current user is the volunteer and the report is in 'reported' status
    if request.user.volunteer and report.status == 'reported':
        report.status = 'in_progress'
        report.save()
        messages.success(request, 'Report accepted and set to In Progress.')
    else:
        messages.error(request, 'Unable to accept the report.')

    return redirect('dashboard_vol')

@login_required(login_url='login')
def mark_solve(request,report_id):
    report=Report.objects.get(id=report_id)
    if request.user.volunteer and report.status == 'in_progress':
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

def edit_profile(request):
    context={}
    user = request.user

    if hasattr(user, 'organization'):
        user_type = 'organization'
        profile_info = Organization.objects.get(org_name=user)
    else:
        user_type = 'volunteer'
        profile_info = Volunteer.objects.get(vol_name=user)

    if user_type=='organization':
        temp_org=Org_Form(instance=user)
        temp_org_add=Org_AddForm(instance=user.organization)
        if request.method == 'POST':
            temp_org=Org_Form(request.POST,instance=user)
            temp_org_add=Org_AddForm(request.POST,instance=user.organization)
            if temp_org.is_valid() and temp_org_add.is_valid():
                temp_org.save()
                temp_org_add.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('/profile/')
        context={'user_type': user_type,'org':temp_org , 'org_add':temp_org_add,'profile_info': profile_info}

    else:
        temp_vol=Vol_Form(instance=user)
        temp_vol_add=Vol_AddForm(instance=user.volunteer)
        if request.method == 'POST':
            temp_vol=Vol_Form(request.POST,instance=user)
            temp_vol_add=Vol_AddForm(request.POST,instance=user.volunteer)
            if temp_vol.is_valid() and temp_vol_add.is_valid():
                temp_vol.save()
                temp_vol_add.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('/profile/')
        context={'user_type': user_type,'vol':temp_vol , 'vol_add':temp_vol_add,'profile_info': profile_info}

    return render(request, 'edit_profile.html', context)

    


"""def signup_vol(request):
    form=User_vol()
    if request.method == "POST":
        form=User_vol(request.POST)
        if form.is_valid():
            #email = form.cleaned_data['email']
            #org_name = form.cleaned_data['org_name']
            #password = form.cleaned_data['password1']
            
            # Use the create_organization method
            #user = CustomUser.objects.create_volunteer(email=email, org_name=org_name, password=password)
            user_name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            organization= form.cleaned_data.get('organization')
            age= form.cleaned_data.get('age')
            gender= form.cleaned_data.get('gender')
            city= form.cleaned_data.get('city')
            skills= form.cleaned_data.get('skills')
            V=Volunteer(vol_name=user_name,email=email,org_name=organization,age=age,gender=gender,city=city,skills=skills)
            V.save()
            form.save()
            messages.success(request,'Acount is created for ')
            return redirect('/login/') 
    context={}
    return render(request,'signup_vol.html',context)


def signup_org(request):

    form=User_org()
    if request.method == "POST":
        form=User_org(request.POST)
        if form.is_valid():
            #email = form.cleaned_data.get('email')
            #org_name = form.cleaned_data.get('org_name')
            #password = form.cleaned_data.get('password1')
            # Use the create_organization method
            #user = CustomUser.objects.create_user(email=email, username=org_name, password=password, is_organization=True)
            form.save()
            user_name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            domain = form.cleaned_data.get('domain')
            location = form.cleaned_data.get('location')
            level = form.cleaned_data.get('level')

            organization_instance=Organization(
                org_name=user_name,
                email=email,
                domain=domain,
                location=location,
                level=level
                )
            organization_instance.save()
            messages.success(request,'Acount is created for ')
            return redirect('/login/') 
    context={}
    return render(request,'signup_org.html',context)

class reg_org(CreateView):
    form_class= User_org()
    template_name=signup_org.html
    success_url='/login/'
    def form_valid(self, form):
        messages.success(self.request, 'Account is created for {}'.format(form.cleaned_data['org_name']))
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle the case where the form is invalid
        return self.render_to_response(self.get_context_data(form=form)) 


def login_user(request):
    if request.method == "POST":
        username=request.POST.get('username')#bcoz html ma form ma name=username
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user:
            if user.is_staff == True:
                login(request,user)
                return redirect("/dashboard_vol/")
            else:
                login(request,user)
                return redirect("/dashboard_org/")

    return render(request,'login.html')

def dashboard_vol(request):
    report=Report.objects.all()
    report=report.filter(status='reported')
    context={'report':report}

    return render(request,'dashboard_vol.html',context)

def dashboard_org(request):
    report=Report.objects.all()
    report=report.filter(status='reported')
    context={'report':report}

    return render(request,'dashboard_org.html',context)

    """
