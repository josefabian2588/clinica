from django.contrib import admin

# Register your models here.

from .models import Medico
from actions import export_as_excel
from actions import export_as_csv_action

class MedicoAdmin(admin.ModelAdmin):
	list_display = ('codigoMedico_med','Nombre_Medico','Telefono','correo',)
	list_filter =('codigoMedico_med',)
	search_fields = ('numeroCarnet_pac',)
	filter_horizontal =('especialidad',)
	actions = (export_as_excel,)




admin.site.register(Medico,MedicoAdmin)