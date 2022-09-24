from datetime import datetime
from django.db.models import Count
from urllib import response
from apis.models import *
from .serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.db.models import Q

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListUser(generics.ListCreateAPIView):    
    queryset=User.objects.all()
    serializer_class = UserSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializers  
    
    
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListEmployee(generics.ListCreateAPIView):    
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailEmployee(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializers  


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListAppel_offre(generics.ListCreateAPIView):    
    queryset=Appel_offre.objects.all()
    serializer_class = Appel_offreSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailListAppel_offre(generics.RetrieveUpdateDestroyAPIView):
    queryset=Appel_offre.objects.all()
    serializer_class= Appel_offreSerializers  


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListAvis_passation(generics.ListCreateAPIView):    
    queryset=Avis_passation.objects.all()
    serializer_class = Avis_passationSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailAvis_passation(generics.RetrieveUpdateDestroyAPIView):
    queryset=Avis_passation.objects.all()
    serializer_class= Avis_passationSerializers  


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListPpm(generics.ListCreateAPIView):    
    queryset=Ppm.objects.all()
    serializer_class = PpmSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailPpm(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ppm.objects.all()
    serializer_class= PpmSerializers  


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListContrat(generics.ListCreateAPIView):    
    queryset=Contrat.objects.all()
    serializer_class = ContratSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailContrat(generics.RetrieveUpdateDestroyAPIView):
    queryset=Contrat.objects.all()
    serializer_class= ContratSerializers  
    
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListComptabilite(generics.ListCreateAPIView):    
    queryset=Comptabilite.objects.all()
    serializer_class = ComptabiliteSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailComptabilite(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comptabilite.objects.all()
    serializer_class= ComptabiliteSerializers  


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListConge(generics.ListCreateAPIView):    
    queryset=Conge.objects.all()
    serializer_class = CongeSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailConge(generics.RetrieveUpdateDestroyAPIView):
    queryset=Conge.objects.all()
    serializer_class= CongeSerializers  

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListOrdre_mission(generics.ListCreateAPIView):    
    queryset=Ordre_mission.objects.all()
    serializer_class = Ordre_missionSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailOrdre_mission(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ordre_mission.objects.all()
    serializer_class= Ordre_missionSerializers  


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListDocuments(generics.ListCreateAPIView):    
    queryset=Documents.objects.all()
    serializer_class = DocumentsSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailDocuments(generics.RetrieveUpdateDestroyAPIView):
    queryset=Documents.objects.all()
    serializer_class= DocumentsSerializers  
    

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListCourrier(generics.ListCreateAPIView):    
    queryset=Courrier.objects.all()
    serializer_class = CourrierSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailCourrier(generics.RetrieveUpdateDestroyAPIView):
    queryset=Courrier.objects.all()
    serializer_class= CourrierSerializers  