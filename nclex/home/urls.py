from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.user_login, name="user_login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.user_logout, name="user_logout"),
    path('contact/', views.contact, name="contact"),
]
