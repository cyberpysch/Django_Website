from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    #path('blogComment/',views.blogComment,name='blogComment'),
    path('',views.index, name='blog'),
    path('<str:slug>',views.blogPost,name='blogPost'),
]
