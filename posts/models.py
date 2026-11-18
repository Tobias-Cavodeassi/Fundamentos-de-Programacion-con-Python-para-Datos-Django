from django.db import models


# Modelo que representa una publicación del blog
class Post(models.Model):
    # Opciones predefinidas para el estado: (valor guardado, texto que se muestra)
    ESTADOS = [
        ("borrador", "Borrador"),
        ("publicado", "Publicado"),
        ("archivado", "Archivado"),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # se completa sola al crear el post
    estado = models.CharField(max_length=10, choices=ESTADOS, default="borrador")
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)  # imagen opcional

    # Cómo se muestra cada post en el admin y en la consola
    def __str__(self):
        return self.titulo