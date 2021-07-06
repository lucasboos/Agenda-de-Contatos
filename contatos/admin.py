from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao')
    list_display_links = ('id', 'nome')
    # list_filter = ('nome')
    list_per_page = 30
    search_fields = ('nome', 'sobrenome')


# admin.site.register(Categoria) Caso houvesse o administrador criaria.
admin.site.register(Contato, ContatoAdmin)
