from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"