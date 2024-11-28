from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('information/', views.information, name='information'),
    path('location/', views.location, name='location'),
    path('direction/', views.direction, name='direction'),
    path('concierge/', views.concierge, name='concierge'),
    path('smart/', views.smart, name='smart'),
    path('premium/', views.premium, name='premium'),
    path('block/', views.block, name='block'),
    path('dong/', views.dong, name='dong'),
    path('pyeong/', views.pyeong, name='pyeong'),
    path('apply/', views.apply, name='apply'),
]
