from apis.models import  *
from django.contrib import admin


@admin.register(Employee)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['nom']



admin.site.register(passation)
admin.site.register(Ppm)
admin.site.register(Appel_offre)
admin.site.register(Contrat)
admin.site.register(Ordre_mission)
admin.site.register(Comptabilite)
admin.site.register(Documents)
admin.site.register(Conge)
admin.site.register(compta)