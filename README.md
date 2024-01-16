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
  
* Uso de plantilla para reutilizar código (uso de {% block name_block %}{% endblock name_block %})


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