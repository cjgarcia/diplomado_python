import re

email = 'cjgartav@gmail.com'

def contiene(term,palabra):
    obj = re.search(term, palabra)
    print(obj)
    return bool(obj)

def contiene_str(term, palabra):
    pos = palabra.find(term)
    print(pos)
    return  pos > 0

if contiene('gmail', email):
    print('Encontrado')
else:
    print('No encontrado')