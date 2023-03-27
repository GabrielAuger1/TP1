from django.contrib import admin
from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')


class SoumissionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user_id', 'etat', 'description')


class ProfessionnelServiceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'taux_horaire', 'user_id')


admin.site.register(User)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Soumission, SoumissionAdmin)
admin.site.register(ProfessionnelService, ProfessionnelServiceAdmin)

