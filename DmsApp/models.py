from django.db import models,IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission,PermissionsMixin,AbstractBaseUser
from django.utils.translation import gettext_lazy as _
#from .managers import CustomUserManager
# Create your models here.

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
    def __str__(self):
        return self.report_name


class Organization(models.Model):
    LEVEL=(
        ('Local','Local'),('National','National'),('International','International'),('Regional','Regional'),
    )
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    org_name = models.OneToOneField(User,on_delete=models.CASCADE)
    domain = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL)
   

    #groups = models.ManyToManyField('auth.Group', related_name='organization_groups')
    #user_permissions = models.ManyToManyField('auth.Permission', related_name='organization_user_permissions')

    """class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'"""

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
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    vol_name=models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER)
    skills = models.CharField(max_length=20, choices=SKILLS)
    city = models.CharField(max_length=30)
    org_name = models.ForeignKey(Organization, on_delete=models.CASCADE)
    
    #groups = models.ManyToManyField('auth.Group', related_name='volunteer_groups')
    #user_permissions = models.ManyToManyField('auth.Permission', related_name='volunteer_user_permissions')

    """class Meta:
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'"""

    def __str__(self):
        return self.vol_name.username
    
class Resources(models.Model):
    org_name=models.ForeignKey(Organization,on_delete=models.CASCADE)
    resource_name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    ward=models.IntegerField()

    def __str__(self):
        return self.resource_name

"""

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email =models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    
    # Organization Fields   
    org_name = models.CharField(max_length=30, blank=True, null=True, unique=True)
    domain = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    org_level = models.CharField(max_length=20, choices=Organization.LEVEL, blank=True, null=True)

    # Volunteer Fields
    vol_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=Volunteer.GENDER, blank=True, null=True)
    skills = models.CharField(max_length=20, choices=Volunteer.SKILLS, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    org_affiliation = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)

    objects = CustomUserManager()

    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email"""




"""class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        email = self.normalize_email(email)
        
        if extra_fields.get('is_organization'):
            user = Organization(email=email, username=username, **extra_fields)
        else:
            user = Volunteer(email=email, username=username, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)
"""
