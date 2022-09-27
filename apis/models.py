from email.policy import default
from lib2to3.pgen2.token import COLONEQUAL
from operator import truediv
from tabnanny import verbose
from django.db import models

from django.db.models import Q
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10)
    sexe = models.CharField(max_length=10)
    image = models.ImageField(upload_to='static/', default="",null=True)
    description = models.TextField(max_length=400)
    adresse = models.CharField(max_length=100)
    poste = models.CharField(max_length=10)
    date_n = models.DateTimeField()
    def __str__(self):
        return self.user.username
    
class Appel_offre(models.Model):
    sujet = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    adresse = models.CharField(max_length=100)
    poste = models.CharField(max_length=10)
    reference = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
class Avis_passation(models.Model):
    sujet = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    reference = models.CharField(max_length=100)
    date = models.DateTimeField()
    poste = models.CharField(max_length=10)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
class Ppm(models.Model):
    sujet = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    reference = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
class Contrat(models.Model):
    employe = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    sujet = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    reference = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
class Comptabilite(models.Model):
    sujet = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    reference = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
    
class Conge(models.Model):
    employe = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    sujet = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet

class Ordre_mission(models.Model):
    employe = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    sujet = models.CharField(max_length=100)
    objet = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    localisation = models.CharField(max_length=100)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet

class Documents(models.Model):
    
    sujet = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
class Courrier(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    objet = models.TextField(max_length=400)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
