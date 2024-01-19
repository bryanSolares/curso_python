# Para definir una función se utilizar la palabra reservada "def"
# La declaración de una función deberá ser primero y luego su invocación
# En Python hay sobrecarga de métodos o funciones en un archivo

def miFuncion (parametro1, parametro2):
    print(parametro1, parametro2)
    print("Primera función")

def funcionSinParametros():
    print(" Esta es una función sin parámetros")

miFuncion("Parámetro 1", "Parámetro 2")
funcionSinParametros()

print("\n**** Definición de función con parámetros por defecto ****")
def miFuncion(param1, param2 = True):
    print(param1, param2)
    print("Segunda función")

miFuncion("Solares")
miFuncion("Bryan", "Solares")

print("\n**** Utilizando funciones con retorno ****")

def funcionConRetorno(numero1, numero2):
    print("Se hace operación de suma")
    return numero1 + numero2

resultado = funcionConRetorno(10,20)
print(resultado)

print("**** Las funciones pueden retornar múltiples resultado y lo hará en una tupla ****")
def funcionConRetornoDeVariosValores(numero1, numero2):
    resultadoSuma = "Resultado de la suma: " + str(numero1 + numero2)
    resultadoMultiplicacion = "Resultado de la multiplicación: " + str(numero1 * numero2)
    return resultadoSuma, resultadoMultiplicacion

print(funcionConRetornoDeVariosValores(10,20))

print("\n**** Extrayendo resultado en variables individuales ****")
operacion1, operacion2 = funcionConRetornoDeVariosValores(10,20)
print(operacion1, operacion2)

print("\n**** Cuando una función no tiene retorno explicito retornará 'None'")
print(miFuncion("Hola"))

print("\n**** Funciones con cantidad indefinida de parámetros. Se utiliza asterisco")
print("**** Al utiliza un parámetro sin límites este valor será una tupla recibida")
def funcionParametrosIndefinidos(*args):
    print(args)

funcionParametrosIndefinidos("Bryan", "Josue", "Solares", "Pérez")

print("\n**** Funciones combinadas con parámetros determinados e indeterminados")
def funcionMixta(param1, param2, *args):
    print(param1)
    print(param2)
    print(args)

funcionMixta("Bryan", "Josue", "Solares", "Pérez")


print("\n**** Utilizando función enumerate para iteración de listas, tuplas y diccionarios")
lista = ["Bryan", "Josue", "Solares"]
tupla = ("Bryan", "Josue", "Solares")
diccionario = {"nombre": "Bryan", "apellido": "Solares"}
for index, value in enumerate(lista):
    print(index, "--", value)

print("\n")
for index, value in enumerate(tupla):
    print(index, "--", value)

print("\n")
for index, value in enumerate(diccionario):
    print(index, "--", value, ":", diccionario[value])

print("\n**** FUNCIONES KEYWOR ARGUMENTS ****")
print("**** Utilizando dobre asterisco (funciones con capacidad para recibir como parámetros valores de Clave-Valor ****")
print("**** El valor del parámetro recibido se convierte en un diccionario ****")
def funcionV(**parametro):
    print(parametro)

funcionV(valo1="bryan", valor2="Josue", valor3="Solares")