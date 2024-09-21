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

class Add_Resource(ModelForm):
    class Meta:
        model=Resources
        fields='__all__'


class CombinedOrgForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    domain = forms.CharField(max_length=100, required=True)
    location = forms.CharField(max_length=100, required=True)
    level = forms.ChoiceField(choices=Organization.LEVEL, required=True)

class CombinedVolForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=Volunteer.GENDER, required=True)
    skills = forms.ChoiceField(choices=Volunteer.SKILLS, required=True)
    city = forms.CharField(max_length=30, required=True)
    org_name = forms.ModelChoiceField(queryset=Organization.objects.all(), empty_label="Select Organization", required=True)

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UpdateOrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['domain', 'location', 'level']
        widgets = {
            'domain': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
        }

class UpdateVolForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['age', 'gender', 'skills', 'city', 'org_name']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'skills': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'org_name': forms.Select(attrs={'class': 'form-control'}),
        }
