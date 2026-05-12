from django.urls import path,include
from . import views
urlpatterns = [
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('all/', views.all),
    path('/affiche/<int>:id/', views.read),
    path('/update/<int:id>', views.update),
]