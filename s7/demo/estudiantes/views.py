from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Estudiante, Asistencia

class IndexView(View):
    def get(self, request):
        context = {'estudiantes': Estudiante.objects.all()}
        return render(request, 'estudiantes/index.html', context)