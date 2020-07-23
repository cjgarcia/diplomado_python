import re

emails = """
    cjgartav@gmail.com
    pedro@gmail.com
    jesus@live.com
    james@hotmail.com
    miguel@outlook.com
    Crecencio Garcia,
    Pedro Enriquez.
    55
    556
    155
    211
    11

"""

resultados = re.findall('[0-9]+', emails)

total = 0
for n in resultados:
    total += int(n)


print(total)
