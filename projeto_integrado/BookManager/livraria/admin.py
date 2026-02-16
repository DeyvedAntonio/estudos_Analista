from django.contrib import admin                               # type: ignore
from .models import Autor, Livro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    fields = ['nome', 'nacionalidade', 'data_nascimento']
    search_fields = ['nome', 'nacionalidade']


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    fields = ['titulo', 'preco', 'data_publicacao', 'autor']
    search_fields = ['titulo', 'autor']
