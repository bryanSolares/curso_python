# En lugar de utizar catch se utiliza except
'''
La estructura cuenta con 4 partes
1. try
2. except
3. else
4. finally
'''

def divicion(dividendo, divisor):
    try:
        print("El resultado es: ", str(dividendo / divisor))
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

divicion(1, 2)
divicion(4, 0)

print("\n**** Capturando varios tipos de excepciones ****")
print("**** Considerar que el bloque 'else' siempre se ejecutará si no hay excepción ****")
print("**** Considerar que finally siempre se ejecutará siempre, aún cuando haya alguna excepción ****")
def divicionCompleja(dividendo, divisor):
    try:
        print(str(dividendo/divisor))
    except ZeroDivisionError:
        print("Considerar que no se puede dividir entre cero")
    except TypeError:
        print("Considerar que los valores deberán ser de tipo numérico")
    else:
        print("No se puede dividir")
    finally:
        print("Código que siempre se ejecutará")

divicionCompleja(10,20)
divicionCompleja(10,0)
divicionCompleja("uno", "dos")


def funcionConExceptGeneral():
    try:
        print("Hola, este dará un error" + 100)
    except:
        print("Mensaje de captura general cuando no se tiene el tipo de error específico")

funcionConExceptGeneral()