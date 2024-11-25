from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('information/', views.information, name='information'),
    path('location/', views.location, name='location'),
    path('direction/', views.direction, name='direction'),
]
