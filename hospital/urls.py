from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hospital-home'),
    path('bedavailabitlity/', views.bedManagement, name='hospital-bed-availabilty'),
    path('donation', views.donation, name='hospital-blood-plasma-donation'),
]