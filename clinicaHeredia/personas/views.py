from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Persona

# Create your views here.

def persona_view(request,nombre_per):
	
	persona = get_object_or_404(Persona, nombre_per=nombre_per)		

	return HttpResponse('OK')