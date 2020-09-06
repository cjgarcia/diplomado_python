x = [0, 2, 4, 6, 8, 10]
# y = x + 2
y = [2, 4, 6, 8, 10, 12]

def obt_valor_y(valor_x):
    return valor_x + 2

#print(obt_valor_y(12))

valores_y = map(lambda valor_x: valor_x + 2, x)

print(*valores_y, sep=', ')
