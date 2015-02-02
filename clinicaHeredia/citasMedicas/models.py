from django.db import models

# Create your models here.

from pacientes.models import Paciente
from medicos.models import Medico



class CitaMedica(models.Model):
		paciente = models.ForeignKey(Paciente)
		medico = models.ForeignKey(Medico)
	

		
