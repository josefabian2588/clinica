from django.db import models

from personas.models import Persona


# Create your models here.

class Paciente(models.Model):
		numeroCarnet_pac  =models.CharField(max_length=50, unique=True, verbose_name="Numero de Carnet",)
		Enfermedad_pac  = models.CharField(max_length=200,blank=True, verbose_name="Enfermedad",)
		comentario_pac  = models.CharField(max_length=300,blank=True, verbose_name="Comentario",)
		preferencial_pac = models.BooleanField(default=False, verbose_name="Es Preferencial?",)
		persona = models.ForeignKey(Persona)

		def __unicode__(self):
			return "%s %s (%s)"%(self.persona.nombre_per,self.persona.apellidos_per,self.numeroCarnet_pac)