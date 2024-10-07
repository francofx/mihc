from django import forms
from .models import Paciente, HistoriaClinica

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dni', 'fecha_nac', 'telefono', 'obra_social', 'numero_afiliado', 'domicilio', 'email', 'genero']
        widgets = {
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            # Agregar más clases Bootstrap a otros campos si se desea.
        }

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['fecha', 'motivo', 'diagnostico', 'proxima_cita']