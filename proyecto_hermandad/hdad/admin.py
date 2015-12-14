from django.contrib import admin
from hdad.models import *

# Register your models here.


# Para definir como queremos que aparezca la tabla

class CapatazAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos','provincia','poblacion','calle')
    list_filter = ('nombre','apellidos')
    ordering = ('nombre',)
    search_fields = ('nombre',)


class CostaleroAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos','provincia','poblacion','hermandad')
    list_filter = ('nombre','apellidos')
    ordering = ('nombre',)
    search_fields = ('nombre',)


class HermandadAdmin(admin.ModelAdmin):
    list_display = ('nombre','num_hermanos','hermano_mayor','dia_salida','capataz')
    list_filter = ('nombre',)
    ordering = ('nombre',)
    search_fields = ('nombre',)



admin.site.register(Capataz,CapatazAdmin)
admin.site.register(Hermandad,HermandadAdmin)
admin.site.register(Costalero,CostaleroAdmin)


