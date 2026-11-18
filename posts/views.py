from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


# Vista de la página de inicio
def inicio(request):
    return render(request, 'posts/inicio.html')


# Vista de la página "Acerca de"
def acerca(request):
    return render(request, 'posts/acerca.html')


# READ (lista): muestra todos los posts, del más nuevo al más viejo
def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha_creacion")
    return render(request, "posts/lista_posts.html", {"posts": posts})


# READ (detalle): muestra un post; si el id no existe, devuelve un error 404
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


# CREATE: muestra el formulario vacío (GET) o guarda el post nuevo (POST)
def crear_post(request):
    if request.method == "POST":
        # request.FILES contiene la imagen subida
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect("posts:detalle_post", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "posts/post_form.html", {"form": form, "titulo_pagina": "Crear post"})


# UPDATE: carga el formulario con los datos del post (GET) o guarda los cambios (POST)
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:detalle_post", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts/post_form.html", {"form": form, "titulo_pagina": "Editar post"})


# DELETE: muestra la confirmación (GET) y borra el post solo si se confirma (POST)
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("posts:lista_posts")
    return render(request, "posts/post_confirm_delete.html", {"post": post})