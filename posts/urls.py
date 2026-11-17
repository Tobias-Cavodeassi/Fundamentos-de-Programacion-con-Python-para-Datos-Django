from django.urls import path

from . import views

# Nombre de la app: permite usar {% url 'posts:inicio' %} en los templates
app_name = 'posts'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('posts/', views.lista_posts, name='lista_posts'),
]