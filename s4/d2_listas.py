# Crear una lista:

#dias_str = [] # Forma literal
#dias_str = list() # Con el constructor

dias_str = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

# Copiar una lista

"""
    Tenemos varias formas de realizar la copia. Yo le mostrare la más comun. 
    Comentario: Pueden utilizar el metodo ls.copy() o ls[:]
"""


dias_str_copia = list(dias_str) 
print(id(dias_str), id(dias_str_copia))
print(dias_str is dias_str_copia)



# Imprimir la lista en pantalla:
#print(dias_str)


# Obtener un elemento de una lista:
#lunes = dias_str[0]

# Verificar el tipo de dato del elemento:
#print(type(lunes))

# Obtener una porcion de la lista:
# dias_semana_lab = dias_str[:5]
# dias_fin_semana = dias_str[-2:] # Realizar el demo con index negativos

# print("Dias semana: ", dias_semana_lab)
# print("Dias fin de semana: ", dias_fin_semana)

# Unir dos listas en una nueva lista:
#semana = dias_semana_lab + dias_fin_semana

#print("Semana:", semana)

# verificar si un elemento existe en la lista:

# if "lunes" in semana:
#     print('El lunes es parte de la semana')
# if "lunes" in dias_semana_lab:
#     print('El lunes es parte de la semana laboral')
# if "lunes" not in dias_fin_semana:
#     print('El lunes no es parte del fin de semana')

# Contar el numero de veces que un elemento se encuentra en una lista:
martes = dias_str.count("martes")
print("#", martes)

# Iterar sobre los elementos de una lista:

# print("\nIterar sobre la semana")
# for dia in semana:
#     print(dia)

# Eliminar un elemento de una lista en base a su indice:

print(dias_str)

dias_str.pop(5)

print(dias_str)


# Eliminar un elemento de una lista en base a su valor:

print(dias_str)

dias_str.remove("domingo")

print(dias_str)

# Agregar un elemento a la lista, especificando su indice:

print(dias_str)

dias_str.insert(5, "sabado")
#dias_str[5] = "sabado" # Error

print(dias_str)

# Agregar un elemento al final de la lista:

print(dias_str)

#dias_str.append("domingo")
dias_str[-1] = "domingo"
print(dias_str)

