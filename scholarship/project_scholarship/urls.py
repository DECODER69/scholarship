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
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('navbar/', views.navbar, name='navbar'),
    path('logindisplay/', views.logindisplay, name='logindisplay'),
    path('login/', views.login, name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('edit/', views.edit, name='edit'),
    path('admindashboard/',views.admindashboard, name='admindashboard'),
    path('navadmin/',views.navadmin, name='navadmin'),
    path('approval/', views.approval, name='approval'),
    path('update/', views.update, name='update'),
    path('revprofile/<str:id>', views.revprofile, name='revprofile'),
    path('review', views.review, name='review'),
    path('active/', views.active, name='active'),
    path('graduate', views.graduate, name='graduate'),
    path('announcements/', views.announcements, name='announcements'),
    path('student_announce/', views.student_announce, name='student_announce'),
    path('anns/', views.anns, name='anns'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)