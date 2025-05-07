from django.db import models

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=150)
    niveau_etudes = models.CharField(max_length=100)
    etablissement_origine = models.CharField(max_length=150)
    concours_souhaite = models.CharField(max_length=100)

    # Téléversement de fichiers
    extrait_naissance = models.FileField(upload_to='fichiers/')
    certificat = models.FileField(upload_to='fichiers/')
    lettre_motivation = models.FileField(upload_to='fichiers/')
    diplome = models.FileField(upload_to='fichiers/')
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.nom} {self.prenoms}"
