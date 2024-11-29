"""
Definição das visualizações (views) para o aplicativo 'recipes'.

Este módulo contém as funções de visualização responsáveis por renderizar as páginas da aplicação de receitas,
incluindo a página inicial, visualização de uma receita específicae a listagem de receitas por categoria.

Funções de visualização disponíveis:
    - `index`: Exibe a página inicial com todas as receitas publicadas e categorias.
    - `recipe`: Exibe os detalhes de uma receita específica baseada no ID.
    - `category`: Exibe as receitas de uma categoria específica.

A função de visualização de cada página passa o contexto adequado para o template renderizado.
"""

from django.shortcuts import render
from django.templatetags.static import static
from .models import Recipe, Category

# Exibe a página inicial com todas as receitas publicadas e categorias
def index(request):
    """
    Exibe a página inicial do site, listando todas as receitas publicadas e as categorias disponíveis.
    Contexto:
        - `recipes`: Lista de todas as receitas publicadas, ordenadas por ID.
        - `categories`: Lista de todas as categorias de receitas.
    """
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    categories = Category.objects.all().order_by('-id')
    
    # Atribui uma URL de capa para cada receita, ou uma imagem padrão se não houver capa
    for recipe in recipes:
        recipe.cover_url = recipe.cover.url if recipe.cover else static('recipes/images/default-image.png')
    
    return render(request, 'recipes/pages/index.html', context={'recipes': recipes, 'categories': categories})

# Exibe os detalhes de uma receita específica
def recipe(request, id):
    """
    Exibe os detalhes de uma receita específica, incluindo o título, descrição e imagem de capa.

    Parâmetros:
        - id: ID da receita a ser exibida.

    Contexto:
        - `recipe`: A receita especificada pelo ID.
    """
    recipe = Recipe.objects.get(id=id)
    recipe.cover_url = recipe.cover.url if recipe.cover else static('recipes/images/default-image.png')
    
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': recipe})

# Exibe a lista de receitas de uma categoria específica
def category(request, category_id):
    """
    Exibe uma lista de receitas filtradas por categoria, com base no ID da categoria.

    Parâmetros:
        - category_id: ID da categoria cujas receitas serão exibidas.

    Contexto:
        - `recipes`: Lista de receitas associadas à categoria especificada.
        - `category_name`: Nome da categoria sendo exibida.
    """
    category_name = Category.objects.get(id=category_id).name
    recipes = Recipe.objects.filter(category_id=category_id , is_published=True).order_by('-id')
    
    # Atribui uma URL de capa para cada receita, ou uma imagem padrão se não houver capa
    for recipe in recipes:
        recipe.cover_url = recipe.cover.url if recipe.cover else static('recipes/images/default-image.png')
    
    return render(request, 'recipes/pages/list_category.html', context={'recipes': recipes, 'category_name': category_name})
