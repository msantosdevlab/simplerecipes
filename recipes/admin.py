"""
Este módulo registra os modelos para administração no Django e personaliza o painel de administração.

Configurações do painel:
    - `site_header`: Define o cabeçalho do painel de administração.
    - `site_title`: Define o título exibido na aba do navegador.
    - `index_title`: Define o título exibido na página inicial do painel.

Modelos registrados:
    - `Category`: Modelo de categoria de receitas.
    - `Recipe`: Modelo de receita com detalhes como título, tempo de preparo e mais.
"""

from django.contrib import admin
from .models import Category, Recipe

# Personalização do painel de administração
admin.site.site_header = "Simple Recipes"
admin.site.site_title = "Administração do Projeto"
admin.site.index_title = "Bem-vindo ao painel"

# Registro dos modelos
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...