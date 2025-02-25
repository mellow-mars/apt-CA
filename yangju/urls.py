from django.urls import path
from . import views  # views.py가 있어야 함

app_name = "yangju"

urlpatterns = [
    path('', views.index, name='index'),
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
