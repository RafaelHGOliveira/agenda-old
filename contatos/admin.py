from django.contrib import admin
from .models import Categoria, Contato


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id' ,'nome', 'sobrenome', 'telefone' ,
                    'email', 'data_criacao', 'categoria')
    list_display_links = ('id' ,'nome', 'sobrenome',)
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('nome', 'sobrenome',)
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contato, ContatoAdmin)
