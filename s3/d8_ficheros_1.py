from csv import reader

fichero = open('datos_estudiantes.csv').read()

datos_estudiantes_csv = reader(fichero)

for estudiante in datos_estudiantes_csv:
    print(estudiante)