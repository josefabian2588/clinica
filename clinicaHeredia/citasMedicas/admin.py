from django.contrib import admin

# Register your models here.
from .models import CitaMedica
from actions import export_as_excel
from actions import export_as_csv_action



class CitaMedicaAdmin(admin.ModelAdmin):
	list_display = ('paciente' ,'medico' ,'especialidad','fechaHora_cita')
	list_filter =('medico','especialidad','paciente',)
	search_fields = ('medico','especialidad','paciente',)
	actions = (export_as_excel,)




admin.site.register(CitaMedica,CitaMedicaAdmin)