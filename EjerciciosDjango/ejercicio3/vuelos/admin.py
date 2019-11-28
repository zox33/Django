from django.contrib import admin

from .models import Aeropuerto, Vuelo, Cliente, Reserva


class VueloAdmin(admin.ModelAdmin):
    list_display = ('aeropuerto_salida', 'fecha_salida', 'aeropuerto_llegada','fecha_llegada')
    

# Register your models here.

admin.site.register(Aeropuerto)
admin.site.register(Vuelo,VueloAdmin)
admin.site.register(Cliente)
admin.site.register(Reserva)
