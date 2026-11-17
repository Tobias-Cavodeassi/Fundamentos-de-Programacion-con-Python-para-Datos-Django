from django.contrib import admin

from .models import Post


# Configuración de cómo se ve el modelo Post en el panel de administración
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "estado", "fecha_creacion")
    list_filter = ("estado",)
    search_fields = ("titulo", "autor")


admin.site.register(Post, PostAdmin)