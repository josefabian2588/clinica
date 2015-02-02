from django.contrib import admin

# Register your models here.

from .models import Paciente
from actions import export_as_excel
from actions import export_as_csv_action



class PacienteAdmin(admin.ModelAdmin):
	list_display = ('numeroCarnet_pac' ,'Enfermedad_pac' ,'comentario_pac',)
	list_filter =('numeroCarnet_pac','Enfermedad_pac',)
	search_fields = ('numeroCarnet_pac',)
	actions = (export_as_excel,)



admin.site.register(Paciente,PacienteAdmin)