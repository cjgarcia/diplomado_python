personas = {'Roger', 'Pedro', 'Jose', 'Jennifer', 'Rudy', 'William'}
covid19_negativos = {'Pedro', 'Jose', 'Jennifer', 'Rudy'}
covid19_positivos = {'Roger', 'Pedro'}

print("Cantidad de Personas: ", len(personas))
print("Personas: ", personas)

# Unio o conjuncion ( para todo {A} y {B}) { A U B}

# Intersection: Donde convergen los conjuntos, para todo {A} que pertenece a {B}
print("Personas Positivas en COVID19:", personas.intersection(covid19_positivos))

# Diferencia: Donde los elementos de los conjuntos divergen 
print("Personas NO Positivas en COVID19:", personas.difference(covid19_positivos))
