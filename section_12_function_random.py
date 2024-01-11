import random

print("\n**** Obteniendo un elemento aleatoriamente de una lista ****")
lista = ["uno", "dos", "tres", "cuatro", 5,6,7,8,9,True, False, ("uno", "dos", "tres"), {"uno": 1, "dos": 2, "tres": 3}, [100,200,300]]
print(lista)
print(random.choice(lista))

# La principal diferencia entre randint y randrange es como incluyen o no el número final en el resultado entregado. También donde randrange tiene la opción
# de poder entregar un valor de "paso" que indicará el número a entregar divisible en el valor de paso.
print("\n**** Obteniendo un valor entero desde un rango disponible con un inicio y un fin ****")
print(random.randint(1,100))

print("\n**** Obteniendo un valor entero desde un rango disponible con un inicio y un fin ****")
print(random.randrange(0,100,10))

print("\n**** Obteniendo un valor decimal aleatoriamente desde 0 a 1 ****")
print(random.random())

print("\n**** Obteniendo un valor decimal aleatoriamente desde un inicio hasta un fin indicado ****")
print(random.uniform(1,10))

print("\n**** Ejercicio de premios y ganadores ****")
lista_premiso = ["Laptop", "Silla", "Mesa", "Xbox", "PS5", "PC", "MAC", "Mouse", "Teclado", "Pantalla", "Monitor"]

for ganador in range(5):
    premio = random.choice(lista_premiso)
    print(f"Ganador {ganador + 1} se lleva: {premio}")

print("\n**** Ordenando aleatoriamente los elementos de una lista ****")
lista_ordenada = ["Azul", "Blanco", "Coral", "Dorado"]
random.shuffle(lista_ordenada)
print(lista_ordenada)

print("\n**** Extraer 'N' cantidad de elementos es una nueva lista ****")
print(random.sample(lista_ordenada, random.randint(1,3)))
