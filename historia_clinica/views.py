from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Consulta
from django.db.models import Q  
from django.core.paginator import Paginator
from .forms import PacienteForm

def home(request):
    return render(request, 'home.html', {'titulo': 'MiHC', 'bajada': 'Mi propio sistema de control de historias clínicas'})

@login_required
def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_pacientes')  # Redirige al listado de pacientes después de agregar uno nuevo
    else:
        form = PacienteForm()
    return render(request, 'agregar_paciente.html', {'form': form})

# Vista para editar un paciente existente
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listado_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'editar_paciente.html', {'form': form})

@login_required
def listado_pacientes(request):
    query = request.GET.get('q')
    pacientes = Paciente.objects.all()

    if query:
        pacientes = pacientes.filter(Q(apellido__icontains=query) | Q(dni__icontains=query))
    
    paginator = Paginator(pacientes, 10)  # 10 pacientes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listado_pacientes.html', {'page_obj': page_obj})

@login_required
def detalle_paciente(request, dni):
    paciente = get_object_or_404(Paciente, dni=dni)
    consultas = Consulta.objects.filter(paciente=paciente).order_by('fecha')  # Ordenadas cronológicamente
    return render(request, 'detalle_paciente.html', {'paciente': paciente, 'consultas': consultas})

# Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listado_pacientes')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

# Vista de logout
def logout_view(request):
    logout(request)
    return redirect('login')