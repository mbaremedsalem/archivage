from django.contrib import admin
from apis.models import  *


@admin.register(Employee)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['nom']
