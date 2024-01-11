# Estructura de un ciclo for
#Considerar que FOR trabajar sobre elementos iterables

for num in range(10):
    print(num)

for num in range(1,10,3):
    print(num)

lista = ['apple', 'banana', 'cherry']
for fruit in lista:
    print(fruit)

print("**** Imprimiendo tabla de multiplicar *****")
contador = 0
for num in range(1,11):
    for num2 in range(1,11):
        print(f"{num} * {num2} = {num * num2}")
        contador+=1
    print("\n")
print(contador)

# Utilizando While
print("\n**** Utilizando ciclo While *****")

contador = 0
while contador <= 10:
    print(contador)
    contador+=1