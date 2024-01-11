# Creación de una lista (una lista es python es como un arreglo en Javascript)
# Una lista puede contiener elementos de varios tipos
lista_vacia = []
lista_llena = [1,2,3,"a","a","b","c",True, False, [100,200,300,400]]
print(lista_vacia)
print(lista_llena)

#Imprimiendo un elemento específico de la lista (su indice inicial es 0)
print(lista_llena[0]) #Impriendo índice cero
print(lista_llena[-1]) #Imprimiendo índice -1. Inicia desde el final hacía atrás
print(lista_llena[1:3]) #Imprimiendo elemento desde índice 1 hasta el 3
print(lista_llena[:4]) #Imprimiendo desde el inicio de la lista hasta índice 4
print(lista_llena[4:]) # Impriendo desde índice 4 hasta el final


# Obteniendo el tamaño de una lista (Se utiliza una función del Scope Global)
print(len(lista_llena))

# Agregando elemento al final de la lista
lista_vacia.append("elemento")
print(lista_vacia)
# aúnque el índice no exista en la lista, el elemento será agregado al final sin añadir espacios o bloques vacios
lista_vacia.insert(10,"Nuevo")
print(lista_vacia)
print(len(lista_vacia))

# Uniendo o concatenando listas
lista_nueva = lista_vacia + lista_llena
lista_nueva_2 = []
lista_nueva_2.append(lista_nueva) # Utilizando append añadirá una lista como un único elemento
print(lista_nueva)
print(lista_nueva_2)

# Comprobando si un indice de la lista tiene un elemento
print(3 in lista_llena)

# Obtener el índice de un elemento buscado
print(lista_llena.index("a"))

# Contar la cantidad de elementos que se repiten en la lista
print(lista_llena.count("a"))

# Eliminando elementos de la lista
print("Eliminando último elemento de una lista")
lista_llena.pop()
print(lista_llena)
print("Eliminado elemento de posición específicia")
lista_llena.pop(0)
print(lista_llena)
print("Eliminando el primer elemento que coincide con el dato proporcionado")
lista_llena.remove("a")
print(lista_llena)
print("Limpiando la lista completa")
lista_vacia = lista_llena[:]
print(lista_vacia)
lista_vacia.clear()
print(lista_vacia)

print("Invirtiendo el orden de los elementos de la lista")
print(lista_llena)
lista_llena.reverse()
print(lista_llena)

print("Replicando los elementos la cantidad de veces deseada")
lista_numeros = [1,2,3]
lista_numeros *= 5
print(lista_numeros)

print("Ordenando los elementos de una lista")
lista = [1,10,2,9,3,8,4,7,5,6]
lista_letras = ["a","z","b","x","c","y"]
print(lista, lista_letras)
lista.sort()
lista_letras.sort()
print(lista, lista_letras)
print("Ordenando los elementos ascendentemente")
lista.sort(reverse=True)
lista_letras.sort(reverse=True)
print(lista, lista_letras)

print("\n**** Extrayendo elemento en variables individuales ****")
lista_pequenia = ["uno", "dos", "tres"]
elemento1, elemento2, elemento3 = lista_pequenia[0], lista_pequenia[1], lista_pequenia[2]
print(elemento1, elemento2, elemento3)