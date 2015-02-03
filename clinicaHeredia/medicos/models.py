from django.db import models

from personas.models import Persona
from especialidades.models import Especialidad

# Create your models here.


class Medico(models.Model):
		codigoMedico_med =models.CharField(max_length=25, unique=True, verbose_name="Codigo del medico",)
		persona = models.ForeignKey(Persona)
		especialidad = models.ManyToManyField('especialidades.Especialidad',related_name='is_especialidad_of')
		

		def __unicode__(self):
			return "%s %s (%s)"%(self.persona.nombre_per,self.persona.apellidos_per,self.codigoMedico_med)


