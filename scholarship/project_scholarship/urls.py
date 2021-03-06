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
    path('signup/', views.signup, name='signup'),
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
    path('andupdate/', views.andupdate, name='andupdate'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('sendmail_confirm/', views.sendmail_confirm, name='sendmail_confirm'),
    path('update1/', views.update1, name='update1'),
    path('email/', views.email, name='email'),
    path('xyz_login/', views.xyz_login, name='xyz_login'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('abcregister/', views.abcregister, name='abcregister'),
    path('adregister/', views.adregister, name='adregister'),
    path('nots/', views.nots, name='nots'),
    path('editfile/', views.editfile, name='editfile'),
    path('editable/', views.editable, name='editable'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)