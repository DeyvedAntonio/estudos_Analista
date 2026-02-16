from django.db import models


class Autor(models.Model):

    nome = models.CharField(
        max_length=150,
        verbose_name='Author',
    )
    nacionalidade = models.CharField(
        max_length=150,
        verbose_name='Nacionalidade',
    )
    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento'
    )
    ativo = models.BooleanField(
        verbose_name='Ativo',
        default=True
    )

    def __str__(self) -> str:
        return self.nome


class Livro(models.Model):

    titulo = models.CharField(
        max_length=200,
        verbose_name='Título do Livro'
    )
    preco = models.FloatField(
        verbose_name='Preço do Livro',
        blank=True,
        null=True,
    )
    data_publicacao = models.DateField(
        verbose_name='Data de Publicação',
        blank=True,
        null=True,
    )
    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        related_name='fk_livro_autor',
        verbose_name='Autor do Livro',
    )

    def __str__(self) -> str:
        return f'{self.titulo} - {self.autor}'
