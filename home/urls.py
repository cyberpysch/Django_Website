from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('loginportal/',views.loginportal,name='loginportal'),
    path('checklogout/',views.checklogout,name='checklogout'),
    path('signup/',views.signup,name='signup'),
]
