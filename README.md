# mi-proyecto-final
Nuestro MVT Django

Entrega intermedia del Proyecto Final de Python de Coderhouse.


En esta entrega de MVT se podrá visualizar código de Python en Djando de:

- Vistas
- Formularios
- Modelos
- Templates


Importante: Este ejemplo fue probado con python 3.10.6 y Django 4.0.4


Checkear que tengas Python
Para comenzar primero tienen que asegurarse que tienen instalado, python.

En windows tiene que abrir una terminal cmd o powershell.

`
PS C:\> python --version
Python 3.X.X 
En Linux/Mac tiene que abrir una terminal bash

$ python --version
Python 3.X.X 
`

Si les aparece la versión todo OK pueden seguir. Caso contrario descarguen python desde este link.

Instalar django
En una terminal cmd o powershell desde windows:

C:\> pip install django
Linux/Mac:

$ pip install django
Si no arrojo errores esto es suficiente para poder correr el projecto.

Instalar django bootstrap v5
C:\> pip install django-bootstrap-v5
Linux/Mac:

$ pip install django-bootstrap-v5
Clonar el projecto con git
windows:

C:\> git clone https://github.com/martinezger/mi-primer-mvt.git
Linux/Mac:

$ git clone https://github.com/martinezger/mi-primer-mvt.git
Correr el Servidor
Los siguinetes comandos son analogos en Mac/Linux/Windows:

cd mi-primer-mvt
python manage.py migrate
La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web

python manage.py runserver
Listo ya tenes corriendo el ejemplo.


Para poder visualizar el material debés hacer click en el siguiente link:
http://127.0.0.1:8000/
