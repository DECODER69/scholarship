from dataclasses import field
from os import name
from pyexpat.errors import messages
from django.contrib import messages 
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context
from httplib2 import Authentication

import project_scholarship
# from .models import registration

from .models import extenduser

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.http import FileResponse
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    return render(request, 'activities/index.html')

def registration(request):
    return render(request, 'activities/registration.html')

def dashboard(request):
    status = extenduser.objects.filter(user = request.user)
    return render(request, 'activities/dashboard.html', {'status': status})

def navbar(request):
    return render(request, 'activities/navigation.html')

def register(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST.get('username'),email=request.POST.get('email'))
            return render(request, 'activities/registration.html', {'error': 'User already exists'})
        except:
            department = request.POST.get('department')
            school = request.POST.get('school')
            course = request.POST.get('course')
            year = request.POST.get('year')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            middlename = request.POST.get('middlename')
            extention = request.POST.get('extention')
            birthday = request.POST.get('birthday')
            birthplace = request.POST.get('birthplace')
            religion = request.POST.get('religion')
            cellphone = request.POST.get('cellphone')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            email = request.POST.get('email')
            civil = request.POST.get('civil')
            unit = request.POST.get('unit')
            street = request.POST.get('street')
            barangay = request.POST.get('barangay')
            municipality = request.POST.get('municipality')
            province = request.POST.get('province')
            father = request.POST.get('father')
            fcontact = request.POST.get('fcontact')
            foccupation = request.POST.get('foccupation')
            mother = request.POST.get('mother')
            mcontact = request.POST.get('mcontact')
            moccupation = request.POST.get('moccupation')
            guardian = request.POST.get('guardian')
            gcontact = request.POST.get('gcontact')
            goccupation = request.POST.get('goccupation')
            income = request.POST.get('income')
            picture = request.FILES['picture']
            # UNEXPECTED ERROR == USER
            user = User.objects.create_user( username=username, password=password1,)
            
            data1 = extenduser(picture=picture,department=department, school=school, course=course, year=year, firstname=firstname, lastname=lastname, middlename=middlename, extention=extention, birthday=birthday, birthplace=birthplace, religion=religion, cellphone=cellphone,gender=gender, age=age,email=email, civil=civil, unit=unit, street=street, barangay=barangay, municipality=municipality, province=province,fname=father, fcontact=fcontact, foccupation=foccupation, mname=mother, mcontact=mcontact, moccupation=moccupation, gname=guardian, gcontact=gcontact, goccupation=goccupation, income=income, user=user)
            data1.save()
            auth.login(request, user)
            return redirect('/registration/')
    else:
        return redirect('/registration/')