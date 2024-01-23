# [Curso Python Udemy](https://www.udemy.com/course/mega-curso-de-python-mas-de-63-horas-y-605-videos-en-espanol/)


# Convenciones
* Python utiliza snake_case para la conveción de nombres [Referencia freeCodeCamp](https://www.freecodecamp.org/news/snake-case-vs-camel-case-vs-pascal-case-vs-kebab-case-whats-the-difference/)

# Pendientes a profundizar

* Entender los conceptos fundamentales de Tuplas, Diccionarios, Listas
* Manejo de Archivos con Python
* Métodos Mágicos
* Manejar y comprender correctamente el uso de método super() cuando hay herencia múltiple
* Considerar buscar la funcionalidad y comportamiento de "with"
````
with self.__init_connection() as connection, connection.cursor() as cursor:
````
* Entornos virtuales
* Funcionalidad y objetivo de cada archivo creado en init project
* Profundizar en el contexto de migraciones, comandos ejecutados (muy deficiente en curso)
* Profundizar sobre herramientas:
  1. [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  2. [Django](https://www.djangoproject.com/)
  3. [Pillow](https://pillow.readthedocs.io/en/stable/)
  4. [Django Extensions](https://django-extensions.readthedocs.io/en/latest/)
  5. [Django Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
  6. [Ipython](https://ipython.org/)
  7. [Werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/)
  8. [Mockaroo](https://www.mockaroo.com/)
  9. [RobotFramework](https://robotframework.org/)
  10. [Pygame](https://www.pygame.org/docs/)
  11. [Pandas](https://pandas.pydata.org/)
  
* Uso de plantilla para reutilizar código (uso de {% block name_block %}{% endblock name_block %})
* Profundizar en aprendizaje de expresiones regulares y ejercicios


# Anotaciones Importantes
## POO
* Cuando se hace herencia, posterior a nombrar la clase, dentro de parentesís se coloca la o las clases de donde se heredará  
* Cuando se utiliza el método super ya no es necesario pasar el parámetro self  
* Los métodos mágicos (__init__, __str__, __repr__) son métodos que modifican comportamientos de la clase por defecto (similiar al toString de Java)
* En python no hay atributos de tipo privado sin embargo se tiene la convención de los dos guiones bajos para identificar que algo es privado
````
class Auto:
    __motor = 1200
    marca = "Nissan"
````
* Se pueden hacer desempaquetaciones de dos formas. 
1. Cuando se hace con un asterico se convierte en una tupla o lista
2. Cuando se hace con doble asterisco se convierte en un diccionario
````
    *row -> row = (elem1, elem2, elem3)
    **row -> row = {'id': 1, 'nombre': 'John Doe', 'direccion': '123 Main St', 'telefono': '555-1234'}
````

## Entornos Virtuales
1. Creación de carpeta
2. Ejecución de comando para creación de entorno
````
python -m venv <env_name>
````
3. Ingresar a SubCarpeta **Scripts** y ejecutar comando para activar entorno
````
activate
````
4. Instalar las librerías deseadas según el entorno virtual creación (por ejemplo Django)
````
pip install django
````
5. Cuando se quiera interactura con un entorno asegurarse estar dentro de él
6. Para comprobar los paquetes instalados en el entorno virtual utilizar comando:
````
pi freeze --local
````

# [Django](https://www.djangoproject.com/)
1. Para crear un nuevo proyecto ejecutar comando:
````
django-admin startproject <project name>
````
2. El resultado obtenido con la estructura por defecto:
````
<project name>
|--- manage.py
|--- <project name>
|    |--- __init__.py
|    |--- asgi.py
|    |--- settings.py
|    |--- urls.py
|    |--- wsgi.py
````
3. Para ejecutar el servidor del proyecto sería:
````
python manage.py runserver
````
4. Según el curso estos son los propósitos de cada archivo.
   * \__init__.py = Archivo que ayuda a inicializar todos los módulos del proyecto
   * settings.py = Configuraciones del proyecto (como conexión a base de datos)
   * urls.py = ruteo de proyecto
   * asgi.py = según curso no se toca
   * wsgi.py = según curso no se toca
5. Dentro de cada proyecto, posterior a inicializarlo se crean aplicaciones o módulos
````
python manage.py startapp <app_name>
````
6. En la estructura de carpeta de un nuevo módulo o app se incluyen nuevos archivos
````
<app name>
|   |--- migrations
|   |--- __init__.py
|--- __init__.py
|--- admin.py
|--- apps.py
|--- models.py
|--- tests.py
|--- views.py
````
7. El esquema utilizado por Djando es:
   * Modelo
   * Vista
   * Template
8. Cuando se crea una nueva app se debe configurar esta app en las configuraciones generales del proyecto.
Nos tendremos que dirigir a la carpeta contenedora general y archivo **settings.py** localizar la lista **INSTALLLED_APPS=[]** y al final de la lista colocar
el nombre de la app que hemos creado.
````
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clientes' #                       <--- aquí
]
````
9. Cuando se crean modelos, es necesario hacer migraciones. Considerar los siguientes comandos:
````
python manage.py migrate
python manage.py makemigrations
````
10. Django cuenta con un administrador por defecto, considerar los siguientes comandos para utilizar la ruta **admin/**
````
python manage.py createsuperuser
````
11. Para hacer una migración o copia de librarías que se están utilizando en un ENV1 a un ENV2 utilizar:
````
pip freeze > requirements.txt
````
12. Cuando se tiene un proyecto con un archivo **requirements.txt** se utiliza el siguiente comando para instalar 
todas las librerías involucradas (el flag -r es para instalación recursiva):
````
pip install -r requirements.txt
````
## ORM
Traductor e intermediario entre base de datos y aplicación. Integra base de datos con la aplicación simplificando
la forma de escribir código sin directamente escribir consultas SQL.  
1. En videos **311** no termina de aclarar y no se entiende la idea de lo que es Shell Plus o Ipython. Solamente considerar los
siguientes comandos:
````
python manage.py shell_plus --print-sql
````
2. Para poder realizar una migración de data desde la funcionalidad de python hacer lo siguiente:
````
# 1. Crear la ubicación donde estará el archivo SQL
# 2. Generar el archivo de migración
python manage.py makemigrations <app_name> --empty
# 3. En archivo generado en las operaciones cargar el archivo SQL que se ejecutará (importante deberá ser un stream)
from django.db import migrations
import os
from crud5.setting import BASE_DIR

def make_migration():
    return open(os.path.join(BASE_DIR, 'migrations/data.sql', 'r')).read()


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(make_migration(),)
    ]

````
3. Finalmente para ejecutar la migración del SQL utilizar:
````
python manage.py sqlmigrate <app_name> <number of file>
python manage.py migrate
````
## Shell Plus
1. Para iniciar Shell Plus se deberá estar en proyecto y ejecutar comando:
````
python manage.py shell_plus --print-sql
````
2. Se puede crear variables dentro de Shell Plus
````
data = <Modelo>.objects.all() # Hará una consulta para capturar todos los registros
data                          # Imprimirá el resultado de la consulta
````
3. Para realizar una consulta con un límite de datos:
````
<Modelo>.objects.all()[:5]
````
4. Llamando columnas específicas de la tabla:
````
<Modelo>.objects.all().values("col1","col2","col3")[:5]
````
5. Haciendo filtrado de información
````
<Modelo>.objects.filter(<columna>=<'data'>).values("col1","col2","col3")[:5]
````
6. Si se quiere integrar funciones personalizadas en Shell Plus
````
# 1. Integrar dentro del modelo una nueva clase que herede de models.Manager
# 2. Crear la función personalizada
# 3. Como la clase está heredando de Manager podremos hacer las operaciones habituales del ORM

from django.db import models

class CustomerManager(models.Manager):
    def get_all(self):
        data = self.all()
        return data
        
# 4. Posterior, en la clase del Model se deberá instanciar la CustomManager

class Customer(models.Model):
....
....
    CustomerManager()
````
7. Cuando se hacen cambios en las clases, estos no son inmediatos en Shell Plus. Para solucionar el problema, dentro de Shell Plus se deberá ejecutar:
````
%load_ext autoreload
%autoreload 2
````
# Pygame
1. Instalación de libraría
````
pip install pygame
````

## Funcionalidad de archivos
1. El archivo **urls.py** contendrá todo el listado de path disponibles para la página o proyecto
2. Cuando se utilian las urls, se deberá contemplar dos datos principales
    * La URL
    * La vista u objeto que retornará un valor de tipo reponse HTTP
````
# urls.py
    from views import *
    
    path('home/', home),
    path('update/<variable>/<int:variable>', update)
    
# views.py
    from django.http import HttpReponse
    
    def home(request):
        return HttpResponse("Hola Mundo")
        
    def update(request, variable, variable: int):
        return HttpResponse(f"Hola Mundo con parámetros {variable} {variable})
````
# [Expresiones Regulares](https://regexr.com/)
## Literal:
abc

## Pattern matching:
.       - Any Character Except New Line  
\d      - Digit (0-9)  
\D      - Not a Digit (0-9)  
\w      - Word Character (a-z, A-Z, 0-9, _)  
\W      - Not a Word Character excluding _  
\s      - Whitespace (space, tab, newline)  
\S      - Not Whitespace (space, tab, newline)  
\t      - Tab  
\n      - New line  

## Grouping:
[]      - Matches Characters in brackets (ranges with -)  
[^ ]    - Matches Characters NOT in brackets  
|       - Or  
( )     - Group  

## Quantifiers:
. *       - 0 or More  
. +       - 1 or More  
?       - 0 or One  
{3}     - Exact Number  
{3,4}   - Range of Numbers (Minimum, Maximum)  
{3,}   	- Range of Numbers (Minimum)  

## Limits:
^       - Beginning of a String  
$       - End of a String  
\b      - Word Boundary  
\B      - Not a Word Boundary  

## Replace:
$0		- Gets all the expression  
$1		- Gets grupo 1 content  

## Ejemplos
````
^\d{4}-\d{4}-\d{4}                              ---> 1234-1234-1234
^\d{4}\s\d{4}\s\d{4}                            ---> 1234 1234 1234
\d{4,6}\s\d{4}\s\d{4,6}                         ---> 123456 123 123456

M\w+                                            ---> Martínez - Mendoza
http[s]?://\w+\.\w+\.\w+(\?\w+=\w+)             ---> https:///www.google.com | http://www.pagina.com?search=word

^\w+@\w+\.\w+(\.\w+)?                           ---> email@email.com
^[a-zA-Z0-9\.\-\_]+@\w+\.\w+(\.\w+)?            ---> algo-2@mail.com | algo.2@mail.com.gt
^[a-zA-Z0-9\.\w\-]+@\w+\.\w+(\.\w+)?            ---> algo_3.2@mail.com

https://git\w+\.\w+/\w+/\w+-win/\w+             ---> https://github.com/docker/for-win/issues
[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+      
\[\d{2}:\d{2}:\d{2}\.\d{3}\]                    ---> 09:00:10.010
\[PowerShell\s+\]                               ---> [PowerShell      ]
\[\d{2}:\d{2}:\d{2}\.\d{3}\]\[P\w+\s+\]         ---> [09:11:10.010][PowerShell      ]
14[56]\s\d{3}\s\d{3}                            ---> 145 567 456 | 146 598 681
(145|146|148)\s\d{3}\s\d{3}                     ---> 145 567 456 | 146 598 681 | 148 567 456
14[^56]\s\d{3}\s\d{3}                           ---> 147 567 456 | 147 995 321 | 148 685 682

(?<=Numero\sde\scuenta\s)(.*?(?=\s))            ---> Numero de cuenta EWD-32d52d-2/34
````

# Pandas (Análisis de Datos)
1. [Documentación](https://pandas.pydata.org/)
2. Instalación de librearías necesaria (pandas y librería para gráficos)
````
pip install pandas matplotlib
````
3. 


# Inconvenientes encontrados
* En video **293** solamente está utiliza una etiqueta 'a' para salir de la sesión, sin embargo esto no fue funcional
se tuvo que hacer un formulario dentro del botón para poder cerrar la sesión. Según información Logout solamente opera con
método POST, al utilizar 'a' genera un petición de tipo GET
* En video **301 - 303** no termina de aclarar el inconveniente con guardar un registro sin foto, sin embargo con investigación se tiene lo siguiente:
````
# En lugar de validar la URL de la foto, se valida el objeto en sí
{% if persona.foto %}
    <td>
        <img src="{{persona.foto.url}}" height="60"/>
    </td>
{% else %}
<td>N/A</td>
{% endif %}
````
* Relacionado al punto anterior hay un inconveniente al eliminar un registro sin foto, la solución al código sería (instructor no soluciona problema):
````
#models.py
    def delete(self, using=None, keep_parents=False):
        if self.foto:
            self.foto.storage.delete(self.foto.name)

        super().delete(using=using, keep_parents=keep_parents)
````
* Sección 37 puede ser desconcertante si no se tiene conocimiento previo. (Comentario personal, no tomar sección si no se e:ntiende el objetivo de la funcionalidad)
* Sección 40: Da una nueva vista para el uso de expresiones regulares sin embargo hubiera sin más útil una implementación con buscador.