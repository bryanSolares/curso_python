texto_minuscula = "este es un texto en minúscula"
texto_mayuscula = "ESTE ES UN TEXTO EN MAYÚSUCULA"


# Primera letra en mayúscula
print("## capitalize ##")
print(texto_minuscula.capitalize())

# Convierte todo a minúscula más avanzado que lower
print("## casefold ##")
print(texto_mayuscula.casefold())

# Convierte todo a minúscula (solamente para caractéres ASCII)
# Mayor rendimiento que casefold
print("## lower ##")
print(texto_mayuscula.lower())
print(texto_minuscula.lower())

# Centra el texto añadiendo el número de espacio indicado a los laterales
print("## center ##")
print(texto_minuscula.center(30))

# Cuenta cantidad de veces que existe el texto o letra indicados
print("## count ##")
print(texto_minuscula.count("es"))
print(texto_minuscula.count("es", 5))

# Devuelve verdadero o falso si el texto termina lo que se indica
print("## endswith ##")
print(texto_minuscula.endswith("texto"))

# Devuelve el indice donde encuentra el texto indicado
print("## find ##")
print(texto_minuscula.find("un", 5))

# Integra al texto valores a partir de variables o indicadores que están incrustados
texto_con_formato_variables = "mi nombre es {nombre} y mi apellido es {apellido}"
texto_con_formato_numeros = "mi nombre es {0} y mi apellido es {1}"
texto_con_formato_vacio = "mi nombre es {} y mi apellido es {}"
print("## format ##")
print(texto_con_formato_variables.format(nombre="Bryan", apellido="Solares"))
print(texto_con_formato_numeros.format("Josué", "Pérez"))
print(texto_con_formato_vacio.format("Bryan Josué", "Solares Pérez"))

# Comprueba si el texto evaluado es en su totalidad alfanumérico
texto_alfanumerico = "Brya28"
texto_no_alfanumerico = "Bryan28@gmail.com"
print("## isalnum ##")
print(texto_alfanumerico.isalnum())
print(texto_no_alfanumerico.isalnum())

# Comprueba si el texto evaluado es completamente alfabético
texto_alfabetico = "Brya"
texto_no_alfabetico = "Bryan28"
print("## isalpha ##")
print(texto_alfabetico.isalpha())
print(texto_no_alfabetico.isalpha())

# Comprueba si el texto está en minúscula
print("### islower ###")
print(texto_minuscula.islower())
print(texto_mayuscula.islower())

# Comprueba si el texto es numérico
print("### isnumeric ###")
print("Texto".isnumeric())
print("123456".isnumeric())
print("-123456".isnumeric())
print("1234.56".isnumeric())

# Comprueba si todo el texto está en mayúscula
print("### isupper ###")
print(texto_minuscula.isupper())
print(texto_mayuscula.isupper())

# Permite unir palabras o texto (considera que se hace por tupla)
texto_tupla = ("Texto1", "Texto2", "Texto3", "Texto4")
texto_arreglo = ["texto1", "texto2", "texto3", "texto4"]
print("### join ###")
print("#".join(texto_tupla))
print("-".join(texto_arreglo))

# Elimina los espacios vacíos del lado izquierdo
print("### lstrip ###")
texto_con_espacios = "       mango         "
print(texto_con_espacios.lstrip())

# En su interior hace un diccionario de datos, donde cada letra es reemplazada por otra deseada
print("### maketrans - translate ###")
texto = "utilizando la función maketrans"
texto_maketrans = texto.maketrans("unc","123")
print(texto_maketrans)
print(texto.translate(texto_maketrans))

# Devuelve una tupla con 3 partes, la primera parte antes del separador, el separador y la segunda parte posterior al separador
print("### partition ###")
texto_partition = "Me gustaría aprender Python"
print(texto_partition.partition("gustaría"))

# Reemplaza los valores de un texto. Se puede indicar cuantas veces se desea que se reemplace un valor
print("### replace ###")
texto_reemplazar = "Este es un texto el cuál se utilizará para reemplazar algo en su interior!"
print(texto_reemplazar.replace("s","S"))
print(texto_reemplazar.replace("e","E", 3))

# Devuelve un arreglo con valores individuales como resultado de la separación a partir del separador indicado. Cuenta con un contador máximo de veces que será separado un valor
print("### split ###")
texto_split = "Este es un texto split"
print(texto_split.split(" "))
print(texto_split.split(" ", 2))

# Devuelve un arreglo con elementos individuales a partir de buscar en el texto un separador de líne (\n)
print("### splitLines ###")
texto_split_lines = "Este es un texto split lines \n Aquí inicia una nueva línea"
print(texto_split_lines.splitlines())

# Elimina los espacios al inicio y al final de un texto. También se le puede indicar un caracter específico que se desea eliminar a los costados
print("### Strip ###")
texto_strip = "    Este es un texto     que contiene      mucho espacios tanto al inicio como al final      ........."
print(texto_strip.strip())
print(texto_strip.strip(". "))

# Invierte los texto de mayúsculas a minúsculas y viceversa
print("### swapcase ###")
texto_swapcase = "Saludos a todos en el curso de Python"
print(texto_swapcase.swapcase())

# Hacer una corrección del todo el texto haciendo que cada inicial sea mayúscula. Convierte las mayúsculas intercarladas a minúsculas
print("### title ###") # -> sALUDOS A TODOS EN EL CURSO DE pYTHON
texto_title = "este es uN curso de Python"
print(texto_title.title()) # -> Este Es Un Curso De Python