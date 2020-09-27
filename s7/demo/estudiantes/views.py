from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Estudiante, Asistencia

class IndexView(View):
    def get(self, request):
        context = {'estudiantes': Estudiante.objects.all()}
        return render(request, 'estudiantes/index.html', context)

class InfoView(View):
    def get(self, request):
        context = {'estudiantes': Estudiante.objects.all() }
        return render(request, 'estudiantes/info.html', context)

class EstudianteNuevo(CreateView):
     model = Estudiante
     fields = '__all__'
     success_url = '/info'

class EstudianteEditar(UpdateView):
     model = Estudiante
     fields = '__all__'
     success_url = '/info'


class EstudianteEliminar(DeleteView):
     model = Estudiante
     fields = '__all__'
     success_url = '/info'

class AsistenciaNueva(CreateView):
    model = Asistencia
    fields = '__all__'
    success_url = '/info'

class LoginView(View):
    def get(self, request):
        return render(request, 'estudiantes/login.html')