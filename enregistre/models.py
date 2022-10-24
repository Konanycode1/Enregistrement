from django.db import models

# Create your models here.

class enregistrement(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    code_ticket = models.CharField(max_length=10)