from django.db import models

# Create your models here.
class Report(models.Model):
    LEVEL=(
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5')
    )
    report_name=models.CharField(max_length=30)
    description=models.CharField(max_length=2056,null=True)
    severity_level=models.CharField(max_length=1,choices=LEVEL)

    def __str__(self):
        return self.report_name

class Organization(models.Model):
    LEVEL=(
        ('Local','Local'),('National','National'),('International','International'),('Regional','Regional'),
    )
    org_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    domain=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    level=models.CharField(max_length=20,choices=LEVEL)

    def __str__(self):
        return self.org_name

class Resources(models.Model):
    org_name=models.ForeignKey(Organization,on_delete=models.CASCADE)
    resource_name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    ward=models.IntegerField()

    def __str__(self):
        return self.resource_name

class Volunteer(models.Model):
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
    )
    SKILLS=(
        ('Time Management','Time Management'),('Fire Safety','Fire Safety'),('Physical Fitness','Physical Fitness')
        ,('Strength','Strength'),('First Aid','First Aid')
    )
    age=models.IntegerField()
    vol_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    gender=models.CharField(max_length=10,choices=GENDER)
    skills=models.CharField(max_length=20,choices=SKILLS)
    city=models.CharField(max_length=30,null=True)
    org_name=models.ForeignKey(Organization,on_delete=models.CASCADE)

    def __str__(self):
        return self.vol_name