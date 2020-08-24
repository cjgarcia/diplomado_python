import json

data_fh = open('data.json').read()
data_json = json.loads(data_fh)

def buscar(nombre):
    item_encontrado = None
    
    for item in data_json:
        if item['nombre'].lower() == nombre.lower():
            item_encontrado = item 

    return item_encontrado

def agregar(**datos):
    datos['monto_pagar'] = datos['cantidad'] * datos['precio']
    data_json.append(datos)


def eliminar(nombre):
    for i in range((len(data_json) - 1)):
        if data_json[i]['nombre'].lower() == nombre.lower():
            del data_json[i]

def guardar():
   fichero_json = open('data.json', 'w')
   str_json = json.dumps(data_json, indent=4)
   fichero_json.write(str_json)
   fichero_json.close()


# Buscar un item
# item = buscar('LECHEX')

# if item:
#     print(item)
# else:
#     print('Item no encontrado')

def mostrar_canasta():
    for item in data_json:
        print(item)

# agregar(nombre='Pizza congelada', cantidad=2, precio=300)
# print("Se ha agregado un nuevo item a la lista")
# mostrar_canasta()


# eliminar('pan')
# print("Se ha eliminado un item a la lista")

# mostrar_canasta()

agregar(nombre='Pan integral', cantidad=5, precio=12)

guardar()
print("Se han guardado los cambios!")

