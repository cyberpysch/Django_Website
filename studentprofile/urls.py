from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    #path(request.user,views.index,name='index'),
    
]
