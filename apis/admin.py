from django.contrib import admin
from apis.models import  *


@admin.register(Employee)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['nom']




admin.site.register(Ppm)
admin.site.register(Appel_offre)


admin.site.register(Contrat)
admin.site.register(Ordre_mission)
admin.site.register(Comptabilite)
admin.site.register(Documents)
admin.site.register(Contrat)
admin.site.register(Conge)