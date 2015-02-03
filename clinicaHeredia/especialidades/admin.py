from django.contrib import admin

# Register your models here.


from .models import Especialidad
from actions import export_as_excel
from actions import export_as_csv_action


class EspecialidadAdmin(admin.ModelAdmin):
	list_display = ('nombre_esp' ,'descripcion_esp' ,)
	search_fields = ('nombre_esp',)
	actions = (export_as_excel,)


admin.site.register(Especialidad,EspecialidadAdmin)

