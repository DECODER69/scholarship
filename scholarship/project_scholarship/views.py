from dataclasses import field
from email import message
from os import name

from django.contrib import messages 
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context
from httplib2 import Authentication
import project_scholarship

from .models import extenduser, Announcement
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
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import login as Login_process 


def index(request):
    return render(request, 'activities/index.html')

def registration(request):
    return render(request, 'activities/registration.html')
def signup(request):
    return render(request, 'activities/signup.html')

def logindisplay(request):
    return render(request, 'activities/login.html')
def navadmin(request):
    return render(request, 'activities/navadmin.html')

def editprofile(request):
    edit = extenduser.objects.filter(user=request.user)
    return render(request, 'activities/editprofile.html', {'edit': edit})

def email(request):
    send = extenduser.objects.filter(status='APPROVED')
    context={
        'send': send,
    }
    return render(request, 'activities/email.html', context)
@login_required(login_url='/')
def dashboard(request):
    status = extenduser.objects.filter(user=request.user)
    count1 = extenduser.objects.filter(status='PENDING').count()
    count2 = extenduser.objects.filter(status='APPROVED').count()
    count3 = extenduser.objects.filter(status='GRADUATED').count()
    context = {
        'status': status,
        'count1':  count1,
        'count2':  count2,
        'count3':  count3,
    }
    return render(request, 'activities/dashboard.html', context)
def navbar(request):
    navdata = extenduser.objects.filter(user=request.user)
    context = {
        'navdata': navdata,
    }
    return render(request, 'activities/navigation.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        middlename = request.POST.get('middlename')
        picture = request.FILES['picture']
     
        if User.objects.filter(username=username).exists():
            messages.error(request, 'ID Number ' + str (username) + ' Already Exist !')
            return redirect('/registration')
        else:
            user = User.objects.create_user(username=username, password=password,)
            datas = extenduser(firstname=firstname, lastname=lastname, middlename=middlename, picture=picture, user=user,)
            datas.save()
            auth.login(request, user)
            messages.info(request, 'Account created successfully')
            return redirect('/registration')
    else:
        return redirect('/registration/')
    
    
    
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None :
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            messages.success(request, 'Incorrect Credentials')
            return render(request, 'activities/index.html')
    else:
        return render(request, 'activities/index.html')
def logout_user(request):
    logout(request)
    return redirect('/')
def edit(request):
    edit = extenduser.objects.filter(user=request.user.id)
    if request.method =='POST':
        department = request.POST.get('department')
        school = request.POST.get('school')
        course = request.POST.get('course')
        year = request.POST.get('year')
        # username = request.POST.get('username')
        # password1 = request.POST.get('password1')
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
        # pictures = request.FILES['pictures']
        extenduser.objects.filter(user=request.user).update(department=department, school=school, course=course, year=year, firstname=firstname, lastname=lastname, middlename=middlename, extention=extention, birthday=birthday, birthplace=birthplace, religion=religion, cellphone=cellphone,gender=gender, age=age,email=email, civil=civil,  barangay=barangay, municipality=municipality, province=province,fname=father, fcontact=fcontact, foccupation=foccupation, mname=mother, mcontact=mcontact, moccupation=moccupation, gname=guardian, gcontact=gcontact, goccupation=goccupation, income=income)
    return render (request, 'activities/editprofile.html', {'edit':edit})

def nots(request):
    return render(request,'activities/not.html')


@login_required(login_url='/xyz_login')
def admindashboard(request):
    if request.user.is_staff:
        count5 = extenduser.objects.filter(status='PENDING').count()
        count6 = extenduser.objects.filter(status='APPROVED').count()
        count7 = extenduser.objects.filter(status='GRADUATE').count()
        context = {
            'count5':  count5,
            'count6':  count6,
            'count7':  count7,
        }
        return render(request,'activities/admindashboard.html',context )
    else:
        messages.error(request, 'Unauthorized User')
        return render(request, 'activities/admin.html')
def approval(request):
    if request.user.is_staff:
        approvals = extenduser.objects.filter(status='PENDING')
        context={
            'approvals': approvals,
        }
        if request.method == 'POST':
            stat1 = request.POST.get('status1')
            stat2 = request.POST.get('getID3')
            if stat1 is not None:
                extenduser.objects.filter(id=stat2).update(status=stat1)
                return redirect('/approval')
            else:
                messages.success(request, 'Please select status')
            print(stat1, stat2)
        return render(request, 'activities/approval.html', context)
    else:
        return render(request, 'activities/admin.html')
def active(request):
    approved = extenduser.objects.filter(status='APPROVED')
    context={
        'approved': approved,
    }
    return render(request, 'activities/approved.html', context)

def graduate(request):
    graduated = extenduser.objects.filter(status='GRADUATE')
    context={
        'graduated': graduated,
    }
    return render(request, 'activities/graduated.html', context)


def update(request):
    if request.method == 'POST':
        stat1 = request.POST.get('status1')
        stat2 = request.POST.get('getID3')
        if stat1 is not None:
            extenduser.objects.filter(id=stat2).update(status=stat1)
            return redirect('/approval')
        else:
            messages.success(request, 'Please select status')
        print(stat1, stat2)
        return redirect('/approval')

def update1(request):
    stat0 = request.POST.get('stats1')
    stat01 = request.POST.get('getID1')

    extenduser.objects.filter(id=stat01).update(status=stat0)
    messages.success(request, 'Status Updated Successfully')

    return redirect('/active')



def revprofile(request, id):
    namess = extenduser.objects.filter(id=id)
    return render(request, 'activities/profiles.html', {'namess': namess})



def review(request):
    return redirect('/revprofile')

def anns (request):
    announcementss = Announcement.objects.all()
    return render(request, 'activities/announcements.html',{'announcementss': announcementss})


def announcements(request):
    if request.method == 'POST':
        dataaaa = request.POST.get('announce_data')
        title = request.POST.get('title')
        cedric = Announcement(content=dataaaa, title=title)
        cedric.save()
     
        return redirect('/anns' )
    else:
        return render(request, 'activities/announcements.html')


def student_announce(request):
    statusx = extenduser.objects.filter(user=request.user)
    data4 = Announcement.objects.all()
    context={
        'statusx': statusx,
        'data4': data4,
    }
    return render (request, 'activities/stud_announcements.html', context)


def andupdate(request):
    if request.method == 'POST':
        anstitle = request.POST.get('anstitle')
        anscontent = request.POST.get('anscontent')
        stats2 = request.POST.get('ansID')
        Announcement.objects.filter(id=stats2) .update(content=anscontent, title=anstitle)
        return redirect('/anns')
    else:
        return redirect('/anns')
    
    
def delete(request, id):
    Announcement.objects.filter(id=id).delete()
    return redirect('/anns')


# EMAILLLLLLLLLLLLLLL
 
def sendmail_confirm( request):
    if request.method == 'POST':
        emails = request.POST.getlist('checked')
        send_mail('e-Scholarship', 
                'Hello this is an email from e-Scholarship. Bigyan ng jacket yaaaan',
                'e-Scholarship',
                ((emails)),
                fail_silently=False)
        messages.success(request, 'Email Sent Successfully')
        print(emails)
    return redirect('/email')


def xyz_login(request):
    if request.user.is_authenticated:
        return redirect('/admindashboard')
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['ausername'], password=request.POST['apassword'])
        if user is not None and user.is_staff:
            auth.login(request, user)
            return redirect('/admindashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'activities/admin.html')

    return render(request, 'activities/admin.html')
def adminlogout(request):
    logout(request)
    return redirect('/xyz_login')

def abcregister(request):
    return render(request, 'activities/admin_reg.html')

def adregister(request):
    if request.method == 'POST':
        adusernames = request.POST.get('adusername')
        adpassword = request.POST.get('adpassword')
        profile = User.objects.create_user(username=adusernames, password=adpassword)
        profile.is_staff = True
        profile.is_superuser = True
        profile.save()
        return redirect('/abcregister')
    else:
        return redirect('/')