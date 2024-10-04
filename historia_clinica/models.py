from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    fecha_nac = models.DateField()
    telefono = models.CharField(max_length=15)
    obra_social = models.CharField(max_length=50)
    numero_afiliado = models.CharField(max_length=50)
    domicilio = models.TextField()
    email = models.EmailField()
    genero = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.TextField()
    diagnostico = models.TextField()
    proxima_cita = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.paciente} - {self.fecha}'
