from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
import mysql.connector as sql
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'activities/index.html')

def registration(request):
    return render(request, 'activities/registration.html')

def register(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'], email=request.POST['email'])
            return render(request, 'activities/signup.html', {'error': 'User already exists'})
        except:
            department = request.POST.get('department')
    return redirect('/registration/')