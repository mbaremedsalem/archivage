from django.contrib import admin
from apis.models import  *


@admin.register(Employee)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Appel_offre)
class ClientAdminapp(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Ppm)
class ClientAdminppm(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Contrat)
class ClientAdmincontrat(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Conge)
class ClientAdminconge(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Contrat)
class ClientAdmincontrat(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Comptabilite)
class ClientAdmincomptabilite(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Documents)
class ClientAdmindocument(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Ordre_mission)
class ClientAdminorder(admin.ModelAdmin):
    search_fields=['nom']