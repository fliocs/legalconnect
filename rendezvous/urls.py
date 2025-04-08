from django.urls import path
from . import views

urlpatterns = [
    path('rdv/', views.liste_rdv, name='liste-rdv'),  # la route pour les rendez-vous
    # Ajouter d'autres routes spécifiques à l'app rendezvous
]