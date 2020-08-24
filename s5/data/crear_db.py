import json, sqlite3, re

# leer fichero json
asistencia_json_fh = open('asistencia.json').read()
asistencia_json = json.loads(asistencia_json_fh)

#print(json.dumps(asistencia_json, indent=4))

# leer el script
crear_tablas_script = open('crear_tablas.sql').read()

# Conex a la base de datos
conn = sqlite3.connect('asistencia_db.sqlite3')
cur = conn.cursor()

# ejecutar script crear tablas
cur.executescript(crear_tablas_script)

# obtener nombre_apellido

def obt_nombre_apellido(valor):
    partes = re.findall('\S+', valor)
    n = len(partes)

    if n == 2:
        return tuple(partes)
    
    elif n == 3:
        return (partes[0], ' '.join(partes[1:]))

    elif n >= 4:
        return (' '.join(partes[:2]), ' '.join(partes[2:]))
    
    else:
        return (valor, 'COMPRAR')
    

#nombre, apellido = obt_nombre_apellido(asistencia_json[0]['Nombre'])

for estudiante in asistencia_json:
    # Param arg, es una buena practica
    #PLAIN OLD Python Object
    
    nombre_apellido = obt_nombre_apellido(estudiante['Nombre'])

    cur.execute(''' 
        INSERT INTO estudiantes(nombre, apellido) VALUES(?, ?);
    ''', nombre_apellido)

    cur.execute(''' SELECT id FROM estudiantes WHERE nombre = ? AND apellido = ?''', 
    nombre_apellido)

    estudiante_id = cur.fetchone()[0]

    # labels semana
    labels_semana = [('S' + str(n)) for n in range(1, 13)]

    for semana in labels_semana:
        if estudiante[semana]:
            cur.execute('''INSERT INTO asistencias(estudiante_id) VALUES(?)''',
             (estudiante_id, ))


# Guarda los cambios en la base de datos
conn.commit()



