from django.db import models


class Membro(models.Model):

    nome = models.CharField(
        max_length=150,
        verbose_name='nome',
        help_text='Nome do Membro da Biblioteca',
    )
    email = models.EmailField(
        verbose_name='e-mail',
        help_text='E-mail do Membro',
        blank=True,
        null=True,
    )
    telefone = models.CharField(
        max_length=20,
        verbose_name='telefone',
        help_text='Telefone de Contato do Membro',
    )
    documento = models.CharField(
        max_length=15,
        verbose_name='documento',
        help_text='Documento do Membro',
    )

    class Meta:
        ordering = ['nome']

    def __str__(self) -> str:
        return f'{self.nome} - {self.telefone}'
