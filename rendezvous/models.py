from django.db import models
from clients.models import Client
from avocats.models import Avocat

class RendezVous(models.Model):
    STATUTS = [('P', 'Planifié'), ('A', 'Annulé'), ('T', 'Terminé')]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    avocat = models.ForeignKey(Avocat, on_delete=models.CASCADE)
    date = models.DateTimeField()
    motif = models.TextField()
    statut = models.CharField(max_length=1, choices=STATUTS, default='P')

    def __str__(self):
        return f"RDV #{self.id} - {self.client} avec {self.avocat}"