from django.forms import ModelForm,PasswordInput
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms 
from django.contrib.auth.models import User


SKILLS=(
        ('Time Management','Time Management'),('Fire Safety','Fire Safety'),('Physical Fitness','Physical Fitness')
        ,('Strength','Strength'),('First Aid','First Aid')
    )
GENDER=(
    ('Male','Male'),
    ('Female','Female'),
)
LEVEL=(
        ('Local','Local'),('National','National'),('International','International'),('Regional','Regional'),
    )
        
class ReportForm(ModelForm):
    class Meta:
        model=Report
        fields='__all__'
        exclude=['status']


class Org_Form(ModelForm):
    password = forms.CharField(widget=PasswordInput()) 
    class Meta():
        model=User
        fields=['username','email','password']
        
class Org_AddForm(forms.ModelForm):
    level = forms.ChoiceField(choices=LEVEL)
    class Meta():
        model=Organization
        fields=['domain','location','level']

class Vol_Form(ModelForm):
    password=forms.CharField(widget=PasswordInput()) 
    class Meta():
        model=User
        fields=['username','email','password']

class Vol_AddForm(forms.ModelForm):
    org_name = forms.ModelChoiceField(queryset=Organization.objects.all(), empty_label="Select Organization")
    skills = forms.ChoiceField(choices=SKILLS)  # Use forms.ChoiceField instead of CharField
    gender = forms.ChoiceField(choices=GENDER)  # Use forms.ChoiceField instead of CharField
    class Meta():
        model=Volunteer
        fields=['org_name','age','gender','city','skills']

"""

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


 class User_vol(UserCreationForm):
    #username=models.CharField( max_length = 50, unique = True)
    #email = models.EmailField(unique = True)
    #password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    org_name=MyModelChoiceField(queryset=Organization.objects.all())
    age=forms.IntegerField()
    gender=forms.ChoiceField(choices=GENDER)
    city=forms.CharField(max_length=30,required=False)
    skills=forms.ChoiceField(choices=SKILLS)
    class Meta:
        model=Volunteer
        fields = ['username', 'email', 'password1', 'password2','org_name','age','gender','city','skills']

class User_org(UserCreationForm):
    #username=models.CharField(max_length = 50, unique = True)
    email = models.EmailField(unique = True)
    #password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #domain=forms.CharField(max_length=100)
    #location=forms.CharField(max_length=100)
    #level=forms.ChoiceField(choices=LEVEL)
    class meta:
        model=Organization
        fields=['username','email','password1','password2','domain','location','level']
"""