class Persona():
    __nombre = None
    apellido = None

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor.title()

cj = Persona()

cj.nombre = "crecencio"
cj.apellido = "Garcia"

print(cj)