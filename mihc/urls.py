from django.contrib import admin
from django.urls import path
from historia_clinica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pacientes/', views.listado_pacientes, name='listado_pacientes'),
]

