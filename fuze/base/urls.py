from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/',views.register,name='register'),
    path('loginn/',views.loginn,name='loginn'),
    path('logout/',views.logout,name='logout'),
    path('index/',views.index,name='index'),
    path('setting/',views.setting,name='setting'),
   
]

