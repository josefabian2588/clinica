from django.db import models

from personas.models import Persona


# Create your models here.

class Paciente(models.Model):
		numeroCarnet_pac =models.CharField(max_length=50)
		Enfermedad_pac = models.CharField(max_length=200)
		comentario_pac = models.CharField(max_length=300)
		persona = models.ForeignKey(Persona)

		def __unicode__(self):
			return "%s %s (%s)"%(self.persona.nombre_per,self.persona.apellidos_per,self.numeroCarnet_pac)