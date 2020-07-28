dias_str = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

"""
    range(valor inicial, valor max, valor de incremento)

    return: iterable, parecido a una lista de números enteros.
"""

for i in range(0, len(dias_str), 2):
    print(dias_str[i])