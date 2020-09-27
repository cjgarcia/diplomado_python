"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from estudiantes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('info/', views.InfoView.as_view(), name='info'),
    path('estudiante/nuevo', views.EstudianteNuevo.as_view(), name='estudiante_nuevo'),
    path('estudiante/<int:pk>/editar', views.EstudianteEditar.as_view(), name='estudiante_editar'),
    path('estudiante/<int:pk>/eliminar', views.EstudianteEliminar.as_view(), name='estudiante_eliminar'),
    path('accounts/login', views.LoginView.as_view(), name='login'),
    path('asistencia/nueva', views.AsistenciaNueva.as_view(), name='asistencia_nueva'),

]
