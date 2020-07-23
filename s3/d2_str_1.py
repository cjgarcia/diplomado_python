email = " cjgartav @ Gmail.com "

email_parts = email.lower().strip().split('@')

usuario = email_parts[0]
nombre_usuario = usuario[:2].upper()
domain_name = email_parts[1].split('.')[0] 
domain = email_parts[1].split('.')[1]


print(nombre_usuario)
print('Usuario:', usuario,'\nDomain Name:', domain_name, '\nDomain:', domain)