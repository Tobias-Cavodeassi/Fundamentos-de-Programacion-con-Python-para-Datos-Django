# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.
Incluye la configuración base del proyecto (`blog_project`) y una aplicación llamada `posts`.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Tobias-Cavodeassi/blog_django.git
```

Entrar a la carpeta del proyecto:

```bash
cd blog_django
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En Windows con Git Bash:

```bash
source venv/Scripts/activate
```

En Linux o macOS:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Aplicar las migraciones (crea la base de datos local):

```bash
python manage.py migrate
```

Crear un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Panel de administración: http://127.0.0.1:8000/admin/ (desde ahí se cargan los posts).

## Ejecución

Levantar el servidor de desarrollo:

```bash
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/

## Aplicaciones

- `posts`: aplicación inicial para manejar las publicaciones del blog. Incluye el modelo Post (título, contenido, autor, fecha de creación y estado), configurado en el panel de administración.

## Páginas disponibles

- `/` : página de inicio.
- `/acerca/` : página "Acerca de".
- `/posts/` : listado de posts (página de ejemplo, sin base de datos todavía).

## Estructura de la app posts

- `views.py`: vistas basadas en funciones que usan `render()`.
- `urls.py`: rutas de la app, conectadas al proyecto con `include()`.
- `templates/posts/`: `base.html` (layout con menú) y las páginas que heredan de él.
- `static/posts/css/estilos.css`: estilos del sitio.

## CRUD de posts

Desde el sitio se pueden gestionar las publicaciones:

- **Listar:** `/posts/`
- **Ver detalle:** `/posts/<id>/`
- **Crear:** `/posts/crear/`
- **Editar:** `/posts/<id>/editar/`
- **Eliminar:** `/posts/<id>/eliminar/` (pide confirmación antes de borrar)

## Manejo de imágenes

- El modelo `Post` tiene un campo `imagen` (`ImageField`), opcional.
- Las imágenes se guardan en la carpeta `media/posts/`, configurada con `MEDIA_URL = '/media/'` y `MEDIA_ROOT = BASE_DIR / 'media'` en `settings.py`.
- En desarrollo, `blog_project/urls.py` sirve los archivos de `media/` cuando `DEBUG` está activo.
- El formulario usa `enctype="multipart/form-data"` y las vistas reciben el archivo con `request.FILES`.

## Dependencia nueva

Se instaló **Pillow**, necesaria para usar `ImageField`. Ya está incluida en `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Cómo probar la carga de imágenes

1. Aplicar las migraciones: `python manage.py migrate`
2. Levantar el servidor: `python manage.py runserver`
3. Entrar a http://127.0.0.1:8000/posts/crear/
4. Completar el formulario, elegir una imagen y guardar.
5. Verificar que la imagen se vea en el detalle del post y que el archivo esté en `media/posts/`.