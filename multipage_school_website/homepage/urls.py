from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home_page, name='homepage'),
    path('about/', views.about_page, name='homepage'),
    path('contact/', views.contact_page, name='homepage'),
    path('homepage/', views.basepage, name='homepage'),
    
]
