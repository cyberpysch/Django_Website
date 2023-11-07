from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='AdmissionPortal'),
    path('contact/',views.contact, name='contact'),
    path('services/',views.services, name='services'), 
]
