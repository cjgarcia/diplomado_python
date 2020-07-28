from pprint import pprint as pp

# Crear un dict 

dias = {} # Forma literal

dias = dict() # Mediante el constructor

# Claves validas

diccionario = {
    26: "hoy",
    '16': "hace 10 dias",
    .5: "la mitad",
    True: 'Siempre cierto' # Conflictivo
}

"""
    La clave de un dict debe ser unica ya que en base a ella accedemos al valor
    del dict. Para garantizar esto, py ejecuta la func hash() sobre cada key o clave
    los valores bool, son parseados a 0 y 1. Así que aunque en teoria podríamos tener 
    True, False, 0 y 1 como claves validas de un dict, en practica tendriamos conflicto. 

    Las listas, dict o cualquier otro objeto no mencionado más arriba, arrojaria un error de hashable 
    al momento de crear un dict
"""

# Crear un dict en base a listas:

dias_str_ls = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
dias_int_ls = [1, 2, 3, 4, 5, 6, 7]

dias_dict = dict(zip(dias_str_ls, dias_int_ls))

# Comenzar con print, luego exportar pprint
# pp(dias, indent=4)
# pp(dias_dict, indent=4)

# Ejemplo de dict

dia = {
    "id": 1,
    "nombre": "lunes",
}

dias = {
    "lunes" : {
        "id" : 1,
        "nombre": "lunes"
    },
    
    "martes" : {
        "id" : 2,
        "nombre": "martes"
    },
    
    "miercoles" : {
        "id" : 3,
        "nombre": "miercoles"
    },
    
    "jueves" : {
        "id" : 4,
        "nombre": "jueves"
    },
    
    "viernes" : {
        "id" : 5,
        "nombre": "viernes"
    },
    
    "sabado" : {
        "id" : 6,
        "nombre": "sabado"
    },
    
    "domingo" : {
        "id" : 7,
        "nombre": "domingo"
    },
}

resultado = [
    {"dias": dias},
    {"respuesta": "OK"}
]

#pp(resultado[1])

# Crear un dict en base a una lista de claves:

"""
    En ocaciones queremos guardar varios acumuladores 
    y los dicts son la estructura de datos ideal para ello.
"""

score_semanal_total = dict.fromkeys(dias_str_ls, 0)

#pp(score_semanal)

# Crear una lista de scores o puntuaciones (aleatorias)

scores = [(n + 1) for n in range(0, 100, 3)]

import random

random.shuffle(scores)


#pp(scores)

# Asignar un score a un dia:
score_semanal = [{dia:random.choice(scores)} for dia in dias_str_ls for score in scores]

# Obtener total por día:

print("Antes del conteo:")
pp(score_semanal_total)

totales = 0
for dia in score_semanal_total:
    total = sum([sum(score.values()) for score in score_semanal if dia in score])
    score_semanal_total[dia] = total
    totales += total

print("Despues del conteo:")
pp(score_semanal_total)

print("Proporciones:")

score_semanal_total_pc = list(map(lambda v: round((v / totales), ndigits=5) * 100, score_semanal_total.values()))

pp(dict(zip(dias_str_ls, score_semanal_total_pc)))

pp(sum(score_semanal_total_pc))



