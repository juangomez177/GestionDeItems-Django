# Gestión de Ítems - Django

- Aplicación web, escrita en Python y con el uso del framework Django, la cual permite gestionar ítems mediante una interfaz web.
- Adicionalmente, la persistencia es gestionada de manera local, donde Django utiliza una BD SQLite para almacenar los datos.

## Tabla de Contenidos
- [Características](#características)
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Instalación](#instalación)
- [Uso](#uso)
- [Empezar desde Cero](#empezar-desde-cero)

## Características
- Crear, leer, actualizar y eliminar ítems, mediante una interfaz de usuario.

## Requisitos
- Python 3.x
- Django 3.x (o superior)
- Otros módulos especificados en `requirements.txt`

## Configuración del Entorno

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/juangomez177/GestionDeItems-Django.git
   cd GestionDeItems-Django
   
1. **Crea el entorno virtual:**
   ```bash
   python -m venv myEnviroment

3. **Activa el entorno virtual:**
   ```bash
   myEnviroment\Scripts\activate

## Instalación  
4. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   
5. **Realiza las migraciones:**
   ```bash
   python manage.py migrate

## Uso   
6. **Ejecuta el servidor:**
   ```bash
   python manage.py runserver
   ```
El cual sería lanzado en: `http://127.0.0.1:8000/`
   
## Empezar desde Cero  
En caso de que quiera empezar un nuevo proyecto Django desde cero:

1. **Crea el entorno virtual desde una nueva carpeta:**
   ```bash
   python -m venv myEnviroment

2. **Activa el entorno virtual:**
   ```bash
   myEnviroment\Scripts\activate

3. **Instala Django:**
   ```bash
   pip install django
    ```

4. **Crea un nuevo proyecto Django:**

(reemplaza myproject con el nombre que desees)
   ```bash
   django-admin startproject myproject
   cd myproject
   ```

5. **Crea una nueva aplicación:**

(reemplaza myapp con el nombre que desees)
   ```bash
   python manage.py startapp myapp
   ```
   
6. **Configuración del Proyecto:**

Abre el archivo `settings.py` en el directorio `myproject`.
Busca la lista `INSTALLED_APPS` y añade `'myapp'`.
    
   ```bash
   INSTALLED_APPS = [
    ...
    'myapp',
    ]
```

7. **Migraciones de Base de Datos:**

Cuando se crean modelos dentro de `models.py`, es necesario **crear** y **aplicar** la migración de la base de datos, se hace mediante:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
3. **Ejecuta el servidor:**
   ```bash
   python manage.py runserver
   ```
El cual sería lanzado en: `http://127.0.0.1:8000/`

8. **Generar el archivo `requirements.txt`:**

El archivo `requirements.txt` es el que contiene todas las dependencias instaladas dentro del proyecto. 
Estando ubicado dentro de la carpeta myproject, se debe ejecutar:
   ```bash
   pip freeze > requirements.txt
   ```
   
9. **Instalando pip:**

Si el archivo `requirements.txt` no fue creado, posiblemente **pip** no esté instalado. Estando ubicado en el directorio raiz, se debe ejecutar:
   ```bash
   python -m pip install
   ```
   






   
   
   
