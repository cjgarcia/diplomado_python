import re

emails = """
    cjgartav@gmail.com
    pedro@gmail.com
    jesus@live.com
    james@hotmail.com
    miguel@outlook.com
    Crecencio Garcia,
    Pedro Enriquez.

"""

resultados = re.findall('\S+@\S+', emails)

print(resultados)
