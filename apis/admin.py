from apis.models import  *
from django.contrib import admin


@admin.register(Employee)
class ClientAdmin(admin.ModelAdmin):
    search_fields=['nom']




admin.site.register(Ppm)
admin.site.register(Appel_offre)

