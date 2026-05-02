from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='Home' ),
    path('', views.contact, name='contact' ),
    # path('resume', views.resume, name='Resume' )

]
