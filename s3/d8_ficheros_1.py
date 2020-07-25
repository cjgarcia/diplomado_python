from csv import reader

fichero_csv = open('asistencia.csv')
datos = list(reader(fichero_csv))

total_asistencia = 0
for estudiante in datos[1:]:
    total_asistencia += int(estudiante[1])

pc_asistencia_clase_ant = (total_asistencia / len(datos[1:])) * 100

print(f"PC asistencia: {pc_asistencia_clase_ant}%")