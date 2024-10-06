from django.contrib import admin
from django.urls import path, include
from historia_clinica import views
from two_factor.urls import urlpatterns as tf_urls
from historia_clinica.views import listado_pacientes, agregar_paciente


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include(tf_urls)),
    path('pacientes/', listado_pacientes, name='listado_pacientes'),
    path('pacientes/agregar/', agregar_paciente, name='agregar_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
]

