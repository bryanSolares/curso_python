
# Se utilizan operadores de igualdad
# == != <= >= < >

# No hay llaves de apertura para IF, considerar identado

variable_a = "A"
variable_b = "a"

if variable_a == variable_b:
    print(True)
else:
    print(False)

if variable_a != variable_b:
    print(True)
else:
    print(False)

if variable_a > variable_b:
    print(True)
else:
    print(False)

if variable_a < variable_b:
    print(True)
else:
    print(False)

# Para insertar condiciones anidadas utilizar "elif"
print("\n**** Utilizando ELIF ****")
if "Hola" == "Hola":
    print("Hola")
elif variable_a > variable_b:
    print("Variable A es mayor a variable B")
else:
    print("Variable B es mayor a variable A")

# Para utilización de condicionantes de variables se utiliza "and" o "or"
print("\n**** Utilizando and y or ****")
if 1 < 10 and 20 > 10:
 print("Uno es mayor a diez y veinte es mayor a diez")

if 1 == 100 or 10 < 100:
    print("Diez es menor que 100")
else:
    print("Aquí no entrará")

print("\n**** Utilizando if a partir de una lista ****")
if 10 in [1,2,3,4,5,6,7,8,9,10]:
    print("El número existe en lista")
else:
    print("El número no existe en lista")


# Considerar que las comparaciones de texto considera el Orden Lexicográfico para su evaluación.
a = "abc"
b = "abd"

if a == b:
    print("Iguales")
elif a > b:
    print("A mayor a B")
else:
    print("A menor a B")