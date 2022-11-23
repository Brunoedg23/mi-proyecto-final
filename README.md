# mi-proyecto-final - PROYECTO FINAL DEL CURSO DE PYTHON - CODERHOUSE

# Nuestro Proyecto Django: 
Recorriendo Argentina

# Objetivo:
Entrega final del Proyecto Final de BLOG en Python/Django para Coderhouse.

# Descripción del Proyecto:
El proyecto que hemos desarrollado es un Blog de lugares de Argentina; donde cada usuario tiene la posibilidad mediante una registración de crear publicaciones de ciudades/lugares que haya visitado. Todo el contenido podría ser administrado vía login; y en la vista pública el usuario solamente podrá observar los lugares pre-cargados...

# Integrantes del Proyecto:
- Bruno Di Gaetano

# Despliegue de nuestro Blog:
En dicho proyecto se podrá visualizar el código en Python/Django de las siguientes funcionalidades:

- Vistas

- Formularios

- Modelos:
    - User
    - Post

- Templates:
    - templates/auth
        - user_form.html: formulario para actualizar/modificar del profile del usuario logueado. 
    - templates/blog
        - blog_login.html: inicio de sesión.
        - blog_logout.html: salida exitosa de una sesión.
        - index.html: Home del blog.
        - post_confirm_delete.html: confirmación o no de una baja de un post.
        - post_detail.html: visualización del detalle de un post seleccionado anteriormente.
        - post_form.html: formulario de carga/actualización de un post.
        - post_list.html: visualización del listado de los post cargados en el Blog.
    - templates/registration
        - signup.html: registración de los usuarios.

- Herencia:
    - base.html: es nuestra extensión de página para estilos y características generales de todas nuestras páginas; donde se utilizan varios blocks para facilitar las configuraciones del titulo de la página, sección de la página y navegación de todo el proyecto; sumándole toda la definición del CSS.

Importante: Este ejemplo fue probado con Python 3.10.6 y Django 4.1.2.

# Checklist de Validación:

1. Para comenzar tienen que asegurarse de tener instalado: Python.
- En Windows tienen que abrir una terminal cmd o powershell.
```
C:\> python --version
Python 3.X.X 
```

- En Linux/Mac tiene que abrir una terminal bash
```
$ python --version
Python 3.X.X 
```

Si les aparece la versión todo OK pueden continuar. Caso contrario descarguen Python desde este link: https://www.python.org/downloads/

2. Instalar Django
- En una terminal CMD o PowerShell desde Windows:
```
C:\> pip install django
```
- Linux/Mac:
```
$ pip install django
```

Si no arrojo errores esto es suficiente para poder correr el projecto.

3. Instalar Django bootstrap v5
- Windows:
```
C:\> pip install django-bootstrap-v5
```
- Linux/Mac:
```
$ pip install django-bootstrap-v5
```

4. Instalar Django Middleware (Plugin) => Para almacenar Media/Imágenes en Servidor Local
- Windows:
```
C:\>pip install whitenoise
```
- Linux/Mac:
```
$ pip install whitenoise
```

5. Instalar Django Pillow (Plugin) => Para trabajar con Imágenes
- Windows:
```
C:\>pip install Pillow
```
- Linux/Mac:
```
$ pip install Pillow
```

6. Migraciones
Los siguientes comandos son análogos en Mac/Linux/Windows:
```
python manage.py migrate
```
La consola mostrara las migraciones de la base de datos que se realizaron.

5. Luego iniciamos el servidor web
```
python manage.py runserver
```

Listo, ya estás en condiciones de ejecutar el Blog.
 
Para poder visualizar el material debés hacer click en el siguiente link:
http://127.0.0.1:8000/blog

