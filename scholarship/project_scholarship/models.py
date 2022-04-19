import email
from pyexpat import model
from django.db import models

class extenduser(models.Model):
    STATUS = (
    ("PENDING", "PENDING"),
    ("FOR REVIEW", "FOR REVIEW"),
    ("APPROVED", "APPROVED"),
    )
    department = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    extention = models.CharField(max_length=100)
    birthday = models.DateField()
    birthplace = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    cellphone = models.IntegerField()
    gender = models.CharField(max_length=10)
    age =  models.DecimalField(max_digits=11, decimal_places=0, default='')
    email = models.EmailField(max_length=254, null=True, unique=True)
    civil = models.CharField(max_length=10)
    unit = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    barangey = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    fcontact =  models.DecimalField(max_digits=11, decimal_places=0, default='')
    foccupation =  models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    mcontact = models.DecimalField(max_digits=11, decimal_places=0, default='')
    moccupation = models.CharField(max_length=100)
    gname = models.CharField(max_length=100)
    gcontact =  models.DecimalField(max_digits=11, decimal_places=0, default='')
    goccupation = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

# Create your models here.
