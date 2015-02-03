from django.db import models

# Create your models here.
class Especialidad(models.Model):
	nombre_esp  = models.CharField(max_length=50,unique=True, verbose_name="Nombre",)
	descripcion_esp = models.CharField(max_length=200,blank=True, verbose_name="Descripcion",)


	def __unicode__(self):
		return self.nombre_esp

			
	