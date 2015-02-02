from django.db import models

# Create your models here.
class Especialidad(models.Model):
	nombre_esp = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre_esp

			
	