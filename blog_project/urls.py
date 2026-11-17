from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Las rutas de la app posts se definen en posts/urls.py
    path('', include('posts.urls')),
]