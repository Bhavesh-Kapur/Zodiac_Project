from django.contrib import admin
from django.urls import path
from HoroscopeApp import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('index/', views.index, name='index'),
]