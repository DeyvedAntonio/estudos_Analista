from django.db import models
from livros.models import Livro
from membros.models import Membro


class Emprestimo(models.Model):

    STATUS_CHOICES = (
        ('Emprestado', 'Emprestado'),
        ('Devolvido', 'Devolvido'),
        ('Atrasado', 'Atrasado'),
    )
    livro = models.ForeignKey(
        Livro,
        on_delete=models.PROTECT,
        related_name='emprestimo_livro',
        verbose_name='livro',
        help_text='Título do Livro',
    )
    membro = models.ForeignKey(
        Membro,
        on_delete=models.PROTECT,
        related_name='emprestar_membro',
        help_text='Pessoa que pegou o livro emprestado',
    )
    data_emprestimo = models.DateField(
        auto_now_add=True,
        verbose_name='data do empréstimo',
        help_text='Data que pegou o livro',
    )
    data_prevista_devolucao = models.DateField(
        blank=True,
        null=True,
        verbose_name='data de devolução',
        help_text='Data de devolução do livro',
    )
    data_devolucao = models.DateField(
        null=True,
        blank=True,
        verbose_name='data da devolução',
        help_text='Data que ocorreu a devolução',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Emprestado',
    )

    class Meta:
        ordering = ['-data_emprestimo',]

    def __str__(self) -> str:
        return f'{self.livro} - Emprestado em: {self.data_emprestimo.strftime("%d/%m/%Y")}'  # NOQA: E501
