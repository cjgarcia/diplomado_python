import os, json

lista_compra = []

while True:
    os.system('cls | clear')
    item_input = input ("Ingrese el nombre del producto o 'parar': ")

    if item_input.upper() == 'PARAR':
        break

    else:
        item = {}
        item['nombre'] = item_input

        try: 
            item['cantidad'] = float(input("Cantidad: "))
            item['precio'] = float(input("Precio: "))
            item['monto_pagar'] = item['cantidad'] * item['precio']
        except:
            item['precio'] = 0

        lista_compra.append(item)


def obt_item_monto_max(canasta):
    item_monto_max = canasta[0]
    for i in range(len(canasta)):
        if i < (len(canasta) - 1):
           if item_monto_max['monto_pagar'] < canasta[i + 1]['monto_pagar']:
               item_monto_max = canasta[i + 1]
    
    return item_monto_max

# print("Nombre", "Cantidad", "Precio", "Monto a Pagar", sep='|\t')

# for item in lista_compra:
#     print(item['nombre'], item['cantidad'], item['precio'], item['monto_pagar'],sep='|\t')



# item_monto_max = obt_item_monto_max(lista_compra)
# print(f"\nEl producto {item_monto_max['nombre']} tiene un monto de {item_monto_max['monto_pagar']} DOP\n")


fichero_json = open('data.json', 'a+')

str_json = json.dumps(lista_compra, indent=4)


fichero_json.write(str_json)

fichero_json.close()

print("Fichero guardado con exito!")


