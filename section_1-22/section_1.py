# Los comentarios de una línea son númeral (#)
"""
Los comentarios con varios líneas son con triple comilla doble (\""")
"""

# Print 
print("Hola Mundo!")

# Creación de variables
nombre_completo = "Bryan Solares"
edad = 18
monto = 3.25
valor_grande = 999_999_999_999_999_999_999
print("Imprimiendo un texto: " + nombre_completo + " tipo de variable " + str(type(nombre_completo)))
print("Imprimiento un entero:" + str(edad) + " tipo de variable " + str(type(edad)))
print("Imprimiendo un double: " + str(monto)  + " tipo de variable " + str(type(monto)))
print("Valor Grande:" + str(valor_grande)  + " tipo de variable " + str(type(valor_grande)))
print("Nombre: " + nombre_completo + " " + "Edad: " + str(edad))

# Números, operaciones matemáticas
operacion_matematica = 10 * (5-3)
obteniendo_numero_entero = 10 // 3
obteniendo_potencia = 10 ** 3 
operacion_compleja = ((3+2)/(2+5) ** 2)
print("Operación Matemática Simple:" + str(operacion_matematica))
print("Obteniendo numero Entero: " + str(obteniendo_numero_entero))
print("Obteniendo Potencia: " + str(obteniendo_potencia))
print("Resolviendo operación compleja: " + str(operacion_compleja))

# Pidiendo valores por consola
nombre = input("Darme  tu nombre: ") # Por defecto siempre será String la devolución del método
print("Nombre por consola: " + str(nombre))

# Métodos de impresión por consola
print("Este es " + "el primer método para imprimir consola")
print("Este es", "el segundo método para imprimir consola")
name = "Bryan"
age = 28
print(f"Nombre: {name} - Edad: {age}")

# Imprimiendo texto replicados
print("Este es un texto replicado" * 10)
texto_replicado = "texto " * 10
print(texto_replicado)

# Métodos de String
frase = "Texto Completo"
extrayendo_5_caracteres = frase[0:5]
extrayendo_desde_el_final = frase[-8:]
dando_vuelta_a_texto = frase[::-1]
print("Extrayendo 5 caracteres desde inicio", extrayendo_5_caracteres)
print("Extrayendo desde el final hacía el inicio:", extrayendo_desde_el_final)
print("Dado vuelta a texto:", dando_vuelta_a_texto)