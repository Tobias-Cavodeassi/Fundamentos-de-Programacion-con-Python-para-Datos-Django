from django.shortcuts import render

from .models import Post


# Vista de la página de inicio
def inicio(request):
    return render(request, 'posts/inicio.html')


# Vista de la página "Acerca de"
def acerca(request):
    return render(request, 'posts/acerca.html')


# Vista del listado: consulta los posts publicados con el ORM, del más nuevo al más viejo
def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)