import random

palabra = 'python'

letras = list(palabra)

random.shuffle(letras)

print('\nPista:', ','.join(letras))

intentos = 3

while intentos:
    print("\nIntentos Disponibles: {}".format(intentos))
    respuesta = input('\nEntra tu respuesta: ')
    if respuesta.lower() == palabra.lower():
        print('\nFelicidades, ganaste :)')
        break
    intentos -= 1
else:
    print('\nPerdiste :(')
