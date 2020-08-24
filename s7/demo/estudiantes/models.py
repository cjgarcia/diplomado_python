from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.timezone import now

class Estudiante(models.Model):
    nombre = models.CharField(
        max_length = 50, 
        help_text = "Agregue su nombre",
        validators = [MinLengthValidator(2, "Debe introducir dos caracteres")]
    )

    apellido = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Asistencia(models.Model):
    fecha = models.DateTimeField("Fecha de la asistencia", default=now)
    estado = models.BooleanField(default=1)

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha}"

