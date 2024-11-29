"""
Definição das rotas (URLs) do aplicativo 'recipes'.

Este módulo mapeia as URLs para as visualizações (views) correspondentes no aplicativo de receitas.

URLs disponíveis:
    - `/`: Exibe a página inicial com todas as receitas.
    - `/<int:id>/`: Exibe uma receita específica baseada no ID.
    - `/category/<int:category_id>/`: Exibe todas as receitas de 
        uma categoria específica.

O parâmetro `app_name` é utilizado para o namespace das URLs, 
facilitando a reversão de URLs.
"""

from django.urls import path
from . import views

# Definindo o namespace para as URLs do aplicativo 'recipes'
app_name = 'recipes'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.recipe, name="recipe"),
    path('category/<int:category_id>/', views.category, name="category"),
]
