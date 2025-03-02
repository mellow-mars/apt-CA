from django.urls import path
from . import views

app_name = "cheongju"

urlpatterns = [
    path('', views.index, name='index'),
    path('information/', views.information, name='information'),
    path('location/', views.location, name='location'),
    path('direction/', views.direction, name='direction'),
    path('apply/', views.apply, name='apply'),
    path('of_premium/', views.of_premium, name='of_premium'),
    path('of_block/', views.of_block, name='of_block'),
    path('of_dong/', views.of_dong, name='of_dong'),
    path('of_commu/', views.of_commu, name='of_commu'),
    path('apt_danzi/', views.apt_danzi, name='apt_danzi'),
    path('apt_block/', views.apt_block, name='apt_block'),
    path('apt_dong/', views.apt_dong, name='apt_dong'),
    path('apt_commu/', views.apt_commu, name='apt_commu'),
    path('apt_pyeong/', views.apt_pyeong, name='apt_pyeong'),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
