from django.shortcuts import render


# Vista de la página de inicio
def inicio(request):
    return render(request, 'posts/inicio.html')


# Vista de la página "Acerca de"
def acerca(request):
    return render(request, 'posts/acerca.html')


# Vista del listado de posts (por ahora es una página de ejemplo, sin base de datos)
def lista_posts(request):
    return render(request, 'posts/lista_posts.html')