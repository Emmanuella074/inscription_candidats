from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.inscription_view, name='inscription'),
    path('confirmation/', views.confirmation, name='confirmation'),  # ✅ ajout de la page de confirmation
]
