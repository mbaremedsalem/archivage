from dataclasses import field
import imp
from xml.dom.minidom import Document
from rest_framework import serializers
from apis import models

from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Employee

class Appel_offreSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Appel_offre
        
class Avis_passationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Avis_passation
        
class PpmSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Ppm
        
class ContratSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Contrat
        
class ComptabiliteSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Comptabilite
        
class CongeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Conge
        
class Ordre_missionSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Ordre_mission
        
class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Documents
        
class CourrierSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.Courrier

class PassassionSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.passation

