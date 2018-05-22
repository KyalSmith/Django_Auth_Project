
from django.contrib import admin
from django.urls import path,include
from . import views

app_name='User'

urlpatterns = [
    path('',views.index,name='index'),
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register')
]
