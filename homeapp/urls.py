from django.contrib import admin
from django.urls import path
from homeapp import views

urlpatterns = [
    path('', views.index, name='homeapp'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]
