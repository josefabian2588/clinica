from django.contrib import admin

# Register your models here.

from .models import Medico
from actions import export_as_excel
from actions import export_as_csv_action

class MedicoAdmin(admin.ModelAdmin):
	list_display = ('codigoMedico_med' ,)
	list_filter =('codigoMedico_med',)
	search_fields = ('numeroCarnet_pac',)
	actions = (export_as_excel,)




admin.site.register(Medico)