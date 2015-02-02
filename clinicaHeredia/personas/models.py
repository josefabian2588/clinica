from django.db import models


# Create your models here.

class Persona(models.Model):
	nombre_per = models.CharField(max_length=50)
	apellidos_per = models.CharField(max_length=100)
	cedula_per = models.CharField(max_length=15)
	telefonoPrincipal_per = models.CharField(max_length=15)
	telefonoAuxiliar_per = models.CharField(max_length=15,blank=True)
	correo_per = models.EmailField(max_length=70,blank=True)
	foto_file = models.ImageField(upload_to='personas')

	def __unicode__(self):
		return self.nombre_per
