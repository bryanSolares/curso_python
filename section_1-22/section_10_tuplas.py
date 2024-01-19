# Las tuplas son lista **Inmutables** no pueden utilizarse los métodos append, extend, remove
# Son más rápidas, formatean un String, se puede utilizar con clavez para diccionarios

tupla_textos = ("melón", "papaya", "banana", "sandía")
tupla_numeros = (1,2,3,4,5,6,7,8,9)
tupla_mixta = (1,2,3,"uno", "dos", "tres", True, False, [1,2,3,4,5,6,7,8,9])
print(tupla_textos)
print(tupla_numeros)
print(tupla_mixta)

print("\n**** Extrayendo elemento de posición indicada ****")
print(tupla_textos[0])
print(tupla_numeros[0])
print(tupla_mixta[0:3])
print(tupla_mixta[:3])
print(tupla_mixta[3:])
print(tupla_mixta[-3:])

print("\n**** Extrayendo elemento en variables individuales ****")
fruta1, fruta2, fruta3, fruta4 = tupla_textos
print(fruta1, fruta2, fruta3, fruta4)

print("\n**** Convirtiendo lista a tupla ****")
lista = list(tupla_textos)
print(lista)

print("\n**** Validando si elemento se encuentra en tupla ****")
print("melón" in tupla_textos)
print("piña" in tupla_textos)

print("\n**** Consultando cuantas veces un elemento existe en una tupla ****")
print(tupla_textos.count("melón"))