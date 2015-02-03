from django.contrib import admin

# Register your models here.

from .models import Persona

from actions import export_as_excel
from actions import export_as_csv_action
from sorl.thumbnail import get_thumbnail


class PersonaAdmin(admin.ModelAdmin):
	list_display = ('cedula_per' ,'nombre_per' ,'apellidos_per' ,'telefonoPrincipal_per' ,'telefonoAuxiliar_per','correo_per','imagen_persona')
	list_filter =('nombre_per','cedula_per' ,'telefonoPrincipal_per')
	search_fields = ('nombre_per','cedula_per','telefonoPrincipal_per')
	actions = (export_as_excel,)

	def imagen_persona(self, obj):
		return '<img src="%s">' % get_thumbnail(obj.foto_file, '70x70').url
	imagen_persona.allow_tags=True

admin.site.register(Persona, PersonaAdmin)

