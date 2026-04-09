from django.db import models


class Autor(models.Model):

    nome = models.CharField(
        max_length=150,
        verbose_name='nome',
        help_text='Nome do Autor',
    )
    email = models.EmailField(
        verbose_name='email',
        help_text='E-mail do Autor',
        null=True,
        blank=True,
    )
    telefone = models.CharField(
        max_length=20,
        verbose_name='telefone',
        help_text='Telefone de contato do Autor',
        null=True,
        blank=True,
    )
