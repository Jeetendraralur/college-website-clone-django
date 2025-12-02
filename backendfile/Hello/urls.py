from django.contrib import admin
from django.urls import path, include
from Hello import views

urlpatterns = [
    path('',views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('user/', views.user, name='user'),
    path('mainnet/', views.mainnet, name='mainnet')
]