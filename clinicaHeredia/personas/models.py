from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Persona(models.Model):
	nombre_per = models.CharField(max_length=50, verbose_name="Nombre",)
	apellidos_per = models.CharField(max_length=100, verbose_name="Apellidos",)
	cedula_per = models.CharField(max_length=15, unique=True, verbose_name="Numero Cedula",)
	telefonoPrincipal_per = PhoneNumberField(blank=True, verbose_name="Telefono Principal",)
	telefonoAuxiliar_per = PhoneNumberField(blank=True, verbose_name="Telefono Opcional",)
	correo_per = models.EmailField(max_length=70,blank=True, verbose_name="Correo",)
	foto_file = models.ImageField(upload_to='personas',blank=True, verbose_name="Foto",)
	es_medico_per = models.BooleanField(default=False, verbose_name="Es medico?",)

	def __unicode__(self):
		return self.nombre_per