from django.db import models


class Categoria(models.Model):

    nome = models.CharField(
        max_length=50,
        verbose_name='nome',
        help_text='Nome da Categoria',
    )
    descricao = models.TextField(
        verbose_name='descrição',
        help_text='Descrição da Categoria',
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.nome
