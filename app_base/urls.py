from django.urls import path
from app_base import views

urlpatterns = [
    #inicio Productos artesanales
    path('', views.inicio),
]
