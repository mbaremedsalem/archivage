from django.contrib import admin
from apis.models import  *


@admin.register(Employee)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(Appel_offre)
class ClientAdminapp(admin.ModelAdmin):
    search_fields=['nom']


