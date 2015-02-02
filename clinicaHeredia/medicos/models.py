from django.db import models

from personas.models import Persona

# Create your models here.


class Medico(models.Model):
		codigoMedico_med =models.CharField(max_length=30)
		persona = models.ForeignKey(Persona)

		def __unicode__(self):
			return "%s %s (%s)"%(self.persona.nombre_per,self.persona.apellidos_per,self.codigoMedico_med)


