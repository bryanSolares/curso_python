
# Considerar que cuando se hace una suma de una lista a otra en realidad se está añadiendo el espacio de memoria y no la lista como tal
# Si se quieren los elementos puramente, se deberá generar una copia para que no genere conflictos de información inesperados
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = []

lista3 += [lista1, lista2]
print(lista3)
lista1.append(10)
print(lista3)