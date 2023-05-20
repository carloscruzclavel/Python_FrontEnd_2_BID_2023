comandos django:

verificar que la versión de python sea por lo menos 3.7

Menu->Terminal->New Terminal
$ python --version

Crear el entorno virtual
$ python -m venv env

Seleccionar el interprete del entorno virtual
crtl + shift + P
Buscamos: python select interpreter
De la lista elegimos el interprete del entorno virtual (env)

La primera vez es necesario activar desde PowerShell la ejecucion de scripts
Ejecutamos el PowerShell en windows como administrador 
$ Set-ExecutionPolicy Unrestricted -Force
$ Set-ExecutionPolicy Unrestricted -Scope CurrentUser

Activar entorno virtual
Menu->Terminal->New Terminal
o
crtl + shift + p 
buscar Terminal create new integrated terminal

Actualizar pip
python -m pip install --upgrade pip

Instalar django
python -m pip install django

python manage.py runserver

django-admin startproject AerolineaProject


python manage.py makemigrations
python manage.py migrate 

python manage.py createsuperususario

carlos
rnstclvl@gmail.com
312810

making queries django - https://docs.djangoproject.com/en/4.2/topics/db/queries/ -- -pagina donde explican las consultas disponibles

jinja template design  - https://jinja.palletsprojects.com/en/3.1.x/templates/

paginacion: https://docs.djangoproject.com/en/4.2/topics/pagination/