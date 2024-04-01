from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('index.html',views.fun0,name='fun0'),
    path('signupform.html',views.fun1,name='fun1'),
    path('fun1.html',views.sub,name='sub'),
]