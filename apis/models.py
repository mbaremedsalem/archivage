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
    description = models.TextField(max_length=400, default="", editable=False)
    adresse = models.CharField(max_length=100, default="", editable=False)
    poste = models.CharField(max_length=10)
    date_n = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
class Appel_offre(models.Model):
    sujet = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    adresse = models.CharField(max_length=100, default="", editable=False)
    poste = models.CharField(max_length=10)
    reference = models.CharField(max_length=100, default="", editable=False)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
class Avis_passation(models.Model):
    sujet = models.CharField(max_length=100, default="", editable=False)
    description = models.TextField(max_length=400, default="", editable=False)
    reference = models.CharField(max_length=100, default="", editable=False)
    date = models.DateTimeField(auto_now_add=True)
    poste = models.CharField(max_length=10)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
class Ppm(models.Model):
    sujet = models.CharField(max_length=100, default="", editable=False)
    description = models.TextField(max_length=400, default="", editable=False)
    reference = models.CharField(max_length=100, default="", editable=False)
    date_debut = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
class Contrat(models.Model):
    employe = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    sujet = models.CharField(max_length=100, default="", editable=False)
    description = models.TextField(max_length=400, default="", editable=False)
    reference = models.CharField(max_length=100, default="", editable=False)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(auto_now_add=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
class Comptabilite(models.Model):
    sujet = models.CharField(max_length=100, default="", editable=False)
    description = models.TextField(max_length=400, default="", editable=False)
    reference = models.CharField(max_length=100, default="", editable=False)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
    
class Conge(models.Model):
    employe = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    sujet = models.CharField(max_length=100, default="", editable=False)
    reference = models.CharField(max_length=100, default="", editable=False)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet

class Ordre_mission(models.Model):
    employe = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    sujet = models.CharField(max_length=100, default="", editable=False)
    objet = models.CharField(max_length=100, default="", editable=False)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(auto_now_add=True)
    localisation = models.CharField(max_length=100, default="", editable=False)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet

class Documents(models.Model):
    
    sujet = models.CharField(max_length=100, default="", editable=False)
    reference = models.CharField(max_length=100, default="", editable=False)
    description = models.TextField(max_length=400, default="", editable=False)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
    
class Courrier(models.Model):
    sender = models.CharField(max_length=100, default="", editable=False)
    receiver = models.CharField(max_length=100, default="", editable=False)
    titre = models.CharField(max_length=100, default="", editable=False)
    reference = models.CharField(max_length=100, default="", editable=False)
    objet = models.TextField(max_length=400, default="", editable=False)
    file = models.FileField(upload_to ='static/')
    def __str__(self):
        return self.sujet
