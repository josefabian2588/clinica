from django.contrib import admin

# Register your models here.

from .models import Persona

from actions import export_as_excel
from actions import export_as_csv_action


class PersonaAdmin(admin.ModelAdmin):
	list_display = ('cedula_per' ,'nombre_per' ,'apellidos_per' ,'telefonoPrincipal_per' ,'telefonoAuxiliar_per','correo_per','foto_file')
	list_filter =('nombre_per','cedula_per' ,'telefonoPrincipal_per')
	search_fields = ('nombre_per','cedula_per','telefonoPrincipal_per')
	actions = (export_as_excel,)


admin.site.register(Persona, PersonaAdmin)

