from django.urls import path
from . import views
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.urls import include, re_path


app_name = 'activities'

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
]