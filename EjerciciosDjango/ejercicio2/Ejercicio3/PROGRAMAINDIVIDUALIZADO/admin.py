from django.contrib import admin

# Register your models here.
from .models import Residente,Informe,Familiar,ParteInforme

class ParteInformeAdmin(admin.ModelAdmin):
    list_display = ('tipo','informe')


admin.site.register(Residente)
admin.site.register(Informe)
admin.site.register(Familiar)
admin.site.register(ParteInforme,ParteInformeAdmin)