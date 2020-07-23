import re

email = """
    cjgartav@gmail.com
    pedro@gmail.com
    jesus@live.com
    james@hotmail.com
    miguel@outlook.com
"""

def contiene(term,palabra):
    obj = re.search(term, palabra)
    print(obj)
    return bool(obj)


if contiene('gmail', email):
    print('Encontrado')
else:
    print('No encontrado')