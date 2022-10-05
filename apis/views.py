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
class ListPassassion(generics.ListCreateAPIView):    
    queryset=passation.objects.all()
    serializer_class = PassassionSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailPassassion(generics.RetrieveUpdateDestroyAPIView):
    queryset=passation.objects.all()
    serializer_class= PassassionSerializers  

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListCompta(generics.ListCreateAPIView):    
    queryset=compta.objects.all()
    serializer_class = comptaSerializers

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DetailCompta(generics.RetrieveUpdateDestroyAPIView):
    queryset=compta.objects.all()
    serializer_class= comptaSerializers 

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


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def loginclient(request):
    uuu = request.data['username']
    ppp = request.data['password']
    null=None
    try:
        u=authenticate(username=uuu,password=ppp)
    except:
        return Response(
            {
                'status': False,
                'message': 'no client for this information',
                'data': null
            },
            status.HTTP_200_OK
        )
        
    try:
        
        login(request,u)
        try:
            token = Token.objects.get(user=u)
        except:
            token = Token.objects.create(user=u)

        return Response(
            {
                'id':u.id,
                'status': True,
                'token': str(token),
                'message':'login success',
                'data':{
                    'username':u.username
                }
            },
            status.HTTP_200_OK
        )
    except:
        return Response(
            {
                'status': False,
                'message': 'no client for this information',
                'data': null
            },
            status.HTTP_200_OK
        )

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def updatepassassion(request,id):
    sujet=request.data['sujet']
    reference=request.data['reference']
    numeromarche=request.data['numeromarche']
    financement=request.data['financement']

    pas=passation.objects.get(id=id)
    pas.sujet=sujet
    pas.reference=reference
    pas.numeromarche=numeromarche
    pas.financement=financement
    pas.save()
    return Response(
            {
                'sujet':pas.sujet,
                'financement':pas.financement
            },
            status.HTTP_200_OK
        )

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def updatecompta(request,id):
    montant=request.data['montant']
    beneficiaire=request.data['beneficiaire']
    imf=request.data['imf']
    motif=request.data['motif']
    numfact=request.data['numfact']
    net=request.data['net']
    modepay=request.data['modepay']

    pas=compta.objects.get(id=id)
    pas.montant=montant
    pas.beneficiaire=beneficiaire
    pas.imf=imf
    pas.motif=motif
    pas.numfact=numfact
    pas.net=net
    pas.modepay=modepay
    pas.save()
    return Response(
            {
                'mode':pas.modepay,
            },
            status.HTTP_200_OK
        )


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def stat(request):
    pas = passation.objects.count()
    com=compta.objects.count()
    return Response(
            {
                'pas':pas,
                'com':com
            },
            status.HTTP_200_OK
        )