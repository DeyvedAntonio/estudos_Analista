from django.db import models

from autores.models import Autor
from categorias.models import Categoria


class Livro(models.Model):

    titulo = models.CharField(
        max_length=100,
        verbose_name='título',
        help_text='Título do Livro'
    )
    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        related_name='autor_livro',
        verbose_name='Autor',
        help_text='Nome do Author do Livro',
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='categoria_livro',
        verbose_name='categoria',
        help_text='Nome da Categoria do Livro',
    )
    isbn = models.CharField(
        unique=True,
        max_length=100,
        verbose_name='ISBN',
        help_text='Número Único de identificação do Livro',
    )
    ano_publicacao = models.IntegerField(
        verbose_name='ano publicação',
        help_text='Ano de Publicação do Livro',
    )
    quantidade_total = models.IntegerField(
        verbose_name='quantidade total',
        help_text='Quantidade total de livros comprados',
    )
    quantidade_disponivel = models.IntegerField(
        verbose_name='quantidade disponível',
        help_text='Quantidade de Livros disponíveis para empréstimos',
    )

    def __str__(self) -> str:
        return f'{self.titulo} - Autor: {self.autor}'
