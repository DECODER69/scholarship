import email
from pyexpat import model
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class extenduser(models.Model):
    status = models.CharField(max_length=20, default="PENDING")
    department = models.CharField(max_length=100 , default="", null=True)
    school = models.CharField(max_length=100 , default="", null=True)
    course = models.CharField(max_length=100 , default="", null=True)
    year = models.CharField(max_length=100 , default="", null=True)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    extention = models.CharField(max_length=100, default="", null=True)
    birthday = models.CharField(blank=True, default='', null=True, max_length=100,)
    birthplace = models.CharField(max_length=100)
    religion = models.CharField(max_length=100, default="", null=True)
    cellphone = models.CharField(max_length=100, null=True, default="+63 ")
    gender = models.CharField(max_length=10,  null=True)
    age =  models.CharField(max_length=100,  null=True)
    email = models.EmailField(max_length=254, null=True, unique=True)
    civil = models.CharField(max_length=10 , default="", null=True)
    barangay = models.CharField(max_length=100 , default="", null=True)
    municipality = models.CharField(max_length=100 , default="", null=True)
    province = models.CharField(max_length=100 , default="", null=True)
    fname = models.CharField(max_length=100 , default="", null=True)
    fcontact =  models.CharField(max_length=100, null=True, default="+63 ")
    foccupation =  models.CharField(max_length=100 , default="", null=True)
    mname = models.CharField(max_length=100 , default="", null=True)
    mcontact = models.CharField(max_length=100, null=True, default="+63 ")
    moccupation = models.CharField(max_length=100 , default="", null=True)
    gname = models.CharField(max_length=100 , default="", null=True)
    gcontact =  models.CharField(max_length=100, null=True, default="+63 ")
    goccupation = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/', default="", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

# Create your models here.


class Announcement(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

