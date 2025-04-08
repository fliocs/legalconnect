from django.shortcuts import render
from .models import RendezVous

def liste_rdv(request):
    rdvs = RendezVous.objects.filter(statut='P')
    return render(request, 'rendezvous/liste.html', {'rdvs': rdvs})