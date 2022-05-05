from dataclasses import field
from os import name

from django.contrib import messages 
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context
from httplib2 import Authentication
from matplotlib.pyplot import title

import project_scholarship
# from .models import registration

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


# Create your views here.
def index(request):
    return render(request, 'activities/index.html')

def registration(request):
    return render(request, 'activities/registration.html')

def logindisplay(request):
    return render(request, 'activities/login.html')
def navadmin(request):
    return render(request, 'activities/navadmin.html')

def editprofile(request):
    edit = extenduser.objects.filter(user=request.user)
    
    
    return render(request, 'activities/editprofile.html', {'edit': edit})

@login_required(login_url='/logindisplay')
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
        user = request.POST['username']
        if User.objects.filter(username=user).exists():
            messages.info(request, 'Username already exists')
            return redirect('/registration')
        else:
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
    
    
    
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
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
        # pictures = request.FILES['pictures']
        
        extenduser.objects.filter(user=request.user).update(department=department, school=school, course=course, year=year, firstname=firstname, lastname=lastname, middlename=middlename, extention=extention, birthday=birthday, birthplace=birthplace, religion=religion, cellphone=cellphone,gender=gender, age=age,email=email, civil=civil, unit=unit, street=street, barangay=barangay, municipality=municipality, province=province,fname=father, fcontact=fcontact, foccupation=foccupation, mname=mother, mcontact=mcontact, moccupation=moccupation, gname=guardian, gcontact=gcontact, goccupation=goccupation, income=income)
    return render (request, 'activities/editprofile.html', {'edit':edit})


def admindashboard(request):
    
    count5 = extenduser.objects.filter(status='PENDING').count()
    count6 = extenduser.objects.filter(status='APPROVED').count()
    count7 = extenduser.objects.filter(status='GRADUATE').count()
    context = {
     
        'count5':  count5,
        'count6':  count6,
        'count7':  count7,
    }

    return render(request,'activities/admindashboard.html',context )


def approval(request):
    approvals = extenduser.objects.filter(status='PENDING')
    context={
        'approvals': approvals,
    }
    return render(request, 'activities/approval.html', context)

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
    stat1 = request.POST.get('stats')
    stat2 = request.POST.get('getID')

    extenduser.objects.filter(id=stat2).update(status=stat1)
    print(stat1, stat2)
    return redirect('/approval')



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

def sendmail_confirm(request):
 
   
    var = 'Good Day MR/MS '+ name + '\n'+ '\n' + 'This is to confirm your application for Provincial Scholarship has been Approved ! Please wait for an Announcements on your portal. Thank you!'
    message_sent = var
    subject_sent = 'SCHOLARSHIP'
    recipient_sent = ['christian.rapal@gsfe.tupcavite.edu.ph']
    send_mail(subject_sent, message_sent, 'christianrapal2000@gmail.com', recipient_sent, fail_silently=False,auth_user=None, auth_password=None)
    print('goods')
    return redirect('/active')

def sendmail_denied(name,purp,date,depart,mail):
    print('goods')
    var = 'Good Day MR/MS '+ name + '\n'+ '\n' +  'We would like to inform you on your appointment for' + depart + ' on ' + str(date) +  '\n'+ '\n' + 'has been declined for some reason.' + '\n'+ '\n''If you have any queries feel free to reply to this email.'+'\n' + '\n' +'Thank You!!!'+'\n'+ depart +'\n'+'TUP Cavite'
    message_sent = var
    subject_sent = 'TUPC ONLINE APPOINTMENT'
    recipient_sent = [mail,]
    send_mail(subject_sent, message_sent, 'tupc.online.appointment@gmail.com', recipient_sent, fail_silently=False,)
    print('goods')