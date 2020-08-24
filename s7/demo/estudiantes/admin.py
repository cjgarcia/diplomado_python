from django.contrib import admin
from .models import Estudiante, Asistencia


admin.site.register([Estudiante, Asistencia])
