from django.db import models

# Create your models here.
class Livre(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    titre = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    auteur = models.CharField(max_length = 100)
    date_parution = models.DateField(blank=True, null = True) # défini un champs de type date, pouvant etre null ou ne pas etre rempli
    nombre_pages = models.IntegerField(blank =False) # défini un champs de type entier devant etre obligatoirement rempli
    resume = models.TextField(null = True, blank = True) # défini un champs de type texte long

    def __str__(self):
        chaine = f"{self.titre} écrit part {self.auteur} édité le {self.date_parution}"
        return chaine
