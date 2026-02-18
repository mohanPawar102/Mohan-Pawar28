from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='Home' ),
    # path('contact', views.contact, name='Contact' ),
    # path('resume', views.resume, name='Resume' )

]
