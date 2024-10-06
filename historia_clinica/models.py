from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fecha_nac = models.DateField()
    telefono = models.CharField(max_length=15)
    obra_social = models.CharField(max_length=100)
    numero_afiliado = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=255)
    email = models.EmailField()
    genero = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, related_name='historias_clinicas', on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.TextField()
    diagnostico = models.TextField()
    proxima_cita = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Historia clínica de {self.paciente} - {self.fecha}"
