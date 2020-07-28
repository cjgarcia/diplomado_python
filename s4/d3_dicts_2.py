# Dict con los datos del estudiante
estudiante = {
    "nombre": "Crecencio",
    "apellido": "Garcia",
    "presente": True,
    "codigo": 11515  
}
"""
    De esta forma podemos definir que esta func solo recibe keywrds como arg
    Esta caracteristica es muy conveniente para func que trabajan con muchos args
"""
def mostrar(**datos):
    print(f"Nombre Completo: {datos['nombre']} {datos['apellido']} \nID: {datos['codigo']}")

# Ejecutar de la funcion con un dict como arg
Mostrar(**estudiante)

# Descomponer un dict en varias vars (tuple unpacking)
nombre, apellido, presente, codigo = tuple(estudiante.values())

# Imprimo el valor del nombre
print(nombre)

# Ejecutar la func con keywords en vez de un dict
mostrar(nombre = "CJ", apellido = "Garcia", presente=False, codigo=15151)





