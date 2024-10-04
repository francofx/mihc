from django.shortcuts import render
from .models import Paciente

def home(request):
    return render(request, 'home.html', {'titulo': 'MiHC', 'bajada': 'Mi propio sistema de control de historias clínicas'})

def listado_pacientes(request):
    pacientes = Paciente.objects.all()  # Obtén todos los pacientes de la base de datos
    return render(request, 'listado_pacientes.html', {'pacientes': pacientes})
