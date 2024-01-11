
'''
PRIMERA FORMA DE PODER INVOCAR FUNCIONES O VARIABLES DE UNA DECLARACIONES DE ARCHIVO EN OTRO LUGAR
'''
# Importanto el archivo que contiene las funciones o variables
import importaciones

# Llamanda una variables del archivo importado
print(importaciones.pi)

areaCirculo = importaciones.areaCirculo(5)
print(areaCirculo)