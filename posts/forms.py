from django import forms

from .models import Post


# Formulario basado en el modelo Post: genera los campos automáticamente
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "estado", "imagen"]
        widgets = {
            "contenido": forms.Textarea(attrs={"rows": 8}),
        }