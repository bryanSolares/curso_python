
# Un texto es tomado como un arrreglo. Utilizando las llaves se pueden extraer caracteres desde un inicio hasta un fin determinado
# No es obligatorio colocar un inicio o un final, puede ser uno de los dos
texto = "lorem ipsum dolor sit amet, consectetur adip"
print("Extrayendo desde 0 hasta posición 10 ->", texto[0:10])
print("Extrayendo desde 0 hasta posición 10 ->", texto[:10])
print("Extrayendo desde 10 hasta el final ->", texto[10:])
print("Extrayendo desde la posición -10 hasta el final ->", texto[-10:])

# Utilizando "espace" para incluir dobles comillas
texto_escape = "Curso de 'Python'"
texto_escape_2 = "Curso de \"Python\""
print(texto_escape)
print(texto_escape_2)