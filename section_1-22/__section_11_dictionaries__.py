import random

# Los diccionarios son como los objetos de Javascript

diccionario = {
    "nombre": "bryan",
    "apellido": "solares",
    "edad": 28,
    "activo": True,
    "lista": [1,2,3,4,5,6,7,8,9]
}
print(diccionario)

# Para consultar un elemento, es como en Javascript exceptuando el hecho de la utilización directa del punto para acceder a elemento solamente por llaves
print("\n****Extrayendo elemento de un diccionario****")
print(diccionario["nombre"])
print(diccionario["apellido"])

print("\n****Consultando la cantidad de elementos de un diccionario****")
print(len(diccionario))

print("\n****Creando un diccionario utilizando librería random****")
personas = ["Juan", "Roberto", "Ricardo"]
diccionario_descuentos = {variable : random.randint(1,100) for variable in personas}
print(diccionario_descuentos)


## TOMAR EN CONSIDERACIÓN QUE LA FUNCIÓN zip ES UTILIZABLE CON ELEMENTOS ITERABLES Y COMO RESULTADO DEVOLVERÁ UN ELEMENTO ITERABLE
print("\n****Creando lista de tuplas a partir de dos listas con misma cantidad de elementos****")
lista1 = ["Guatemala", "El Salvador", "Honduras", "Nicaragua", "Costa Rica"]
lista2 = [1000,2000,3000,4000,5000]
lista3 = ["Centro", "Sur", "Este", "Oeste", "NorOriente", "NorOccidente"]
lista_poblacion = list(zip(lista1,lista2, lista3))
print(lista_poblacion)

print("\n****Creando diccionario a partir de dos listas diferentes con mismo tamaño****")
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperatura = [10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5]
temperatura_de_semana = {dia: tempe for (dia, tempe) in zip(dias_semana, temperatura)}
print(temperatura_de_semana)

print("\n****Obteniendo nueva lista a partir de evaluar condiciones****")
temperaturas_altas = {dia: tempe for (dia, tempe) in temperatura_de_semana.items() if tempe > 15}
print(temperaturas_altas)

'''
Para comprender a fondo las tuplas, listas y diccionarios en Python, es útil conocer algunos conceptos avanzados y técnicas. Aquí hay algunos temas que podrían considerarse avanzados:

### Para Listas:

1. **Comprensiones de Listas (List Comprehensions):**
   - Las comprensiones de listas son una forma concisa y eficiente de crear listas.
   - Ejemplo: `squares = [x**2 for x in range(10)]`

2. **Funciones de Orden Superior:**
   - Uso de funciones como `map`, `filter`, y `reduce` para operaciones avanzadas en listas.
   - Ejemplo:
     ```python
     numbers = [1, 2, 3, 4, 5]
     doubled = list(map(lambda x: x * 2, numbers))
     ```

3. **Manipulación de Listas:**
   - Métodos avanzados como `sort` con funciones de clave personalizada.
   - Utilización de `sorted` para obtener una nueva lista ordenada.

### Para Tuplas:

1. **Desempaquetado de Tuplas:**
   - Asignación de valores de una tupla a variables individuales.
   - Ejemplo: `a, b, c = (1, 2, 3)`

2. **Tuplas Nombradas (Named Tuples):**
   - Uso de `collections.namedtuple` para crear tuplas con campos con nombre.
   - Facilita el acceso a los elementos por nombre en lugar de índice.

### Para Diccionarios:

1. **Comprensiones de Diccionarios:**
   - Similar a las comprensiones de listas, pero para la creación de diccionarios.
   - Ejemplo: `squared_dict = {x: x**2 for x in range(5)}`

2. **Métodos Avanzados:**
   - Utilización de métodos como `update`, `setdefault`, `pop` para la manipulación de diccionarios.
   - Exploración de métodos específicos para operaciones avanzadas.

3. **Diccionarios por Comprensión (Dictionary Comprehensions):**
   - Creación eficiente de diccionarios mediante expresiones compactas.
   - Ejemplo: `{k: v for k, v in zip(keys, values)}`

4. **Manejo de Claves y Valores:**
   - Entender cómo trabajar con las claves y valores de un diccionario.
   - Concepto de claves inmutables y cómo usar tipos inmutables como claves.

### General:

1. **Iteradores y Generadores:**
   - Comprender cómo funcionan los iteradores y cómo crear generadores para trabajar eficientemente con grandes conjuntos de datos.

2. **Funciones Anónimas (Lambda Functions):**
   - Uso de funciones lambda para operaciones breves y específicas.
   - A menudo se utilizan en combinación con funciones como `map` y `filter`.

3. **Manejo de Errores y Excepciones:**
   - Saber cómo manejar excepciones al trabajar con estructuras de datos para mejorar la robustez del código.

4. **Programación Orientada a Objetos (OOP):**
   - Entender cómo las listas, tuplas y diccionarios son objetos en Python y cómo se pueden aplicar conceptos de OOP al trabajar con ellos.

Estos conceptos avanzados proporcionan un conocimiento más profundo y una mayor capacidad para aprovechar al máximo estas estructuras de datos en Python.
'''
