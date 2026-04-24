from django.contrib import admin

from .models import Membro


class MembroAdmin(admin.ModelAdmin):
    fields = [
        'nome',
        'email',
        'telefone',
        'documento',
    ]
    search_fields = ['nome', 'telefone',]


admin.site.register(Membro, MembroAdmin)
