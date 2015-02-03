from django.db import models

from pacientes.models import Paciente
from medicos.models import Medico
from especialidades.models import Especialidad

# Create your models here.

class CitaMedica(models.Model):
	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)
	especialidad = models.ForeignKey(Especialidad)
	fechaHora_cita = models.DateTimeField()