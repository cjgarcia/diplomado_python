items = [
    {'nombre': 'leche', 'precio':50, 'cantidad': 5},
    {'nombre': 'leche', 'precio':50, 'cantidad': 3},
    {'nombre': 'huevos', 'precio':100, 'cantidad': 2}
]

menor = 0
i = 0

for item in items:
    cantidad = item.get('cantidad', 0)

    if i < 2: 
        i += 1

    cantidad_sig = items[i].get('cantidad', 0)
    
    if cantidad <= cantidad_sig:
        menor = cantidad
    else: 
        menor = cantidad_sig

print(f"Cantidad menor: {menor}")