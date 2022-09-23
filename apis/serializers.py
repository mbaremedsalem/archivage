from dataclasses import field
import imp
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
        model=User

class Appel_offreSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User
        
class Avis_passationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User
        
class PpmSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User
        
class ContratSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User
        
class ComptabiliteSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User
        
class CongeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User
        
class Ordre_missionSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User
        
class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User
        
class CourrierSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=User

