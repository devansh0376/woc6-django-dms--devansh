from django.db import models,IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission,PermissionsMixin,AbstractBaseUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Organization(models.Model):
    LEVEL=(
        ('Local','Local'),('National','National'),('International','International'),('Regional','Regional'),
    )
    org_name = models.OneToOneField(User,on_delete=models.CASCADE)
    domain = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL)

    def __str__(self):
        return self.org_name.username

class Volunteer(models.Model):
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
    )
    SKILLS=(
        ('Time Management','Time Management'),('Fire Safety','Fire Safety'),('Physical Fitness','Physical Fitness')
        ,('Strength','Strength'),('First Aid','First Aid')
    )
    vol_name=models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER)
    skills = models.CharField(max_length=20, choices=SKILLS)
    city = models.CharField(max_length=30)
    org_name = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.vol_name.username
    
class Report(models.Model):
    LEVEL=(
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5')
    )
    STATUS=(
        ('reported','reported'),
        ('in_progress','in_progress'),
        ('solved','solved'),
    )
    status=models.CharField(max_length=50,choices=STATUS,default='reported')
    report_name=models.CharField(max_length=30)
    description=models.CharField(max_length=2056,null=True)
    severity_level=models.CharField(max_length=1,choices=LEVEL)
    volunteer=models.ForeignKey(Volunteer, null=True, blank=True, on_delete=models.SET_NULL, related_name='reports')
    def __str__(self):
        return self.report_name

class Resources(models.Model):
    org_name=models.ForeignKey(Organization,on_delete=models.CASCADE)
    resource_name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    ward=models.IntegerField()

    def __str__(self):
        return self.resource_name