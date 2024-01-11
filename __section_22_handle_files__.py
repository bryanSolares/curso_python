'''
TIPOS DE OPERACIONES EN ARCHIVOS:
w = Crear el archivo y agregar datos. Si el archivo existe lo borrará y lo creará nuevamente
a = Agregar datos al archivo. Si el archivo no existe lo crea y agrega el dato
r = Leer información del archivo
r+ = Leer y escribir en el archivo

Además de los modos anteriores, hay dos modos principales para en la lectura o apertura de un archivo
t = modo texto
b = modo binario

Por defecto cuando en la función open() solo se pasa el la ubicación del archivo tendrá 'rt'

Tomar en cuenta que al final el proceso deseado en un archivo, deberemos cerrar la operacion close()


'''



archivo = open('archivo.txt',"a")
archivo.write("\nNueva Línea")
archivo.close()

archivo = open('archivo.txt')
print(archivo.readline())
print(archivo.readlines())
archivo.close()


lista = ["Texto 1", "Texto 2", "Texto 3"]
try:
    archivo = open('archivo_nuevo.txt', 'w')
    archivo.writelines(linea + '\n' for linea in lista)
    archivo.close()
except:
    print("Archivo ya existe")