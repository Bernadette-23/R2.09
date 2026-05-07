from django.urls import path,include
from . import views
urlpatterns = [
    path('index/', views.index),
    path('formulaire/', views.formulaire),
    path('bonjour/', views.bonjour),
]